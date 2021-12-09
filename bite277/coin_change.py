from typing import List, Tuple
from functools import lru_cache

"""
n = 5 and coins = [1, 2, 5, 10]

>> make_change(n, coins)
4 (five "1", 1+1+1+2, 1+2+2, and one "5") 

>>> make_change(6, coins)
5 
"""


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """
    changes = get_changes_list(n, tuple(coins))
    return len(changes)


    
@lru_cache
def get_changes_list(n: int, coins: Tuple[int]) -> List[List]:
    """
    This script returns all combinations that sum n.
    """
    valid_coins = [valid_coin for valid_coin in coins if valid_coin <= n]
    changes = list()
    for coin in valid_coins:
        if n-coin > 0:
            changes = changes + [[coin]+change for change in get_changes_list(n-coin, tuple(valid_coins))]
        else:
            changes = changes + [[coin,],]
    # remove permutations
    changes_no_permutations = []
    for change in changes:
        if sorted(change) not in changes_no_permutations:
            changes_no_permutations.append(sorted(change))
    return changes_no_permutations

print(5, get_changes_list(5, tuple([1, 2, 5, 10])))