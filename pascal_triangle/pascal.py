from typing import List
from itertools import pairwise


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    # special cases
    if N < 1:
        return []
    if N == 1:
        return [1]
    else:
        current_list = [1,1]
        for i in range(2,N):
            new_list = []
            new_list.append(current_list[0])
            for a,b in pairwise(current_list):
                new_list.append(a+b)
            new_list.append(current_list[-1])
            current_list = new_list
        return current_list
