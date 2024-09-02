from itertools import product

import pytest

from combinations import generate_letter_combinations


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("2", ["a", "b", "c"]),
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        (
            "79",
            [
                "pw",
                "px",
                "py",
                "pz",
                "qw",
                "qx",
                "qy",
                "qz",
                "rw",
                "rx",
                "ry",
                "rz",
                "sw",
                "sx",
                "sy",
                "sz",
            ],
        ),
        (
            "234",
            [
                "adg",
                "adh",
                "adi",
                "aeg",
                "aeh",
                "aei",
                "afg",
                "afh",
                "afi",
                "bdg",
                "bdh",
                "bdi",
                "beg",
                "beh",
                "bei",
                "bfg",
                "bfh",
                "bfi",
                "cdg",
                "cdh",
                "cdi",
                "ceg",
                "ceh",
                "cei",
                "cfg",
                "cfh",
                "cfi",
            ],
        ),
    ],
)
def test_generate_letter_combinations(digits, expected):
    assert generate_letter_combinations(digits) == expected


def test_generate_letter_combinations_repeated_digits():
    assert generate_letter_combinations("222") == [
        "aaa",
        "aab",
        "aac",
        "aba",
        "abb",
        "abc",
        "aca",
        "acb",
        "acc",
        "baa",
        "bab",
        "bac",
        "bba",
        "bbb",
        "bbc",
        "bca",
        "bcb",
        "bcc",
        "caa",
        "cab",
        "cac",
        "cba",
        "cbb",
        "cbc",
        "cca",
        "ccb",
        "ccc",
    ]


def test_generate_letter_combinations_long_input():
    assert generate_letter_combinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    