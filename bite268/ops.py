import timeit

def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    exploration_tree = {1:[],2:[(2,"*2")]}
    explored = {1}
        
    while True:
        temp_tree = dict()
        for result, branch in exploration_tree.items():
            if result not in explored:
                b1, b2 = explore_branch(branch)
                if b1[-1][0] not in explored:
                    temp_tree[b1[-1][0]] = b1
                if b2[-1][0] not in explored:
                    temp_tree[b2[-1][0]] = b2
                explored.add(result)
        exploration_tree.update(temp_tree)
        if n in exploration_tree:
            return len(exploration_tree[n])


def explore_branch(branch):
    last_result, last_op = branch[-1]
    branch1 = branch.copy()
    branch2 = branch.copy()
    branch1.append((last_result*2, "*2"))
    branch2.append((last_result//3, "//3"))
    return branch1,branch2
