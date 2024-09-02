from typing import Union

import pytest

from coins_on_the_table import PENNY, NICKEL, DIME, QUARTER, coins_on_the_table

T_COINS = Union[type(PENNY), type(NICKEL), type(DIME), type(QUARTER)]

T_COINLIST = list[T_COINS]


@pytest.fixture(scope="module")
def coins() -> T_COINLIST:
    return coins_on_the_table()


@pytest.fixture(scope="module")
def coin_value_map() -> dict[T_COINS, float]:
    return {PENNY: 0.01, NICKEL: 0.05, DIME: 0.1, QUARTER: 0.25}


@pytest.mark.parametrize(
    "expected_coin,expected_count",
    [
        (PENNY, 334),
        (NICKEL, 167),
        (DIME, 250),
        (QUARTER, 250),
    ],
)
def test_count_coin_on_table(
    expected_coin: T_COINS, expected_count: int, coins: T_COINLIST
) -> None:

    assert sum(coin == expected_coin for coin in coins) == expected_count


@pytest.mark.parametrize("expected", [99.19])
def test_total_dollar_amount(
    expected: float, coins: T_COINLIST, coin_value_map: dict[T_COINS, float]
) -> None:
    """Calculating the total dollar amount is predicated on the
    correctness of the counts, so it's not even really necessary
    unless we want the student implmentations of Penny, Nickel, Dime
    and Quarter to provide their values.
    """

    total = 0
    for coin in coins:
        for key, value in coin_value_map.items():
            if coin == key:
                total += value

    total = round(total, 2)

    assert total == expected
    