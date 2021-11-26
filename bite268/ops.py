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
    operation_list = [(2,"*2")]
    
    
    while len(operation_list) < 10000:
        last_result, last_operation = operation_list[-1]
        result_set = {result for result,__ in operation_list}
        if last_result < n and last_result*2 not in result_set:
            operation_list.append((last_result*2,"*2"))
        elif last_result > n and last_result//3 not in result_set:
            operation_list.append((last_result//3,"//3"))
        elif last_result == n:
            return len(operation_list)
        elif last_result//3 in result_set or last_result*2 in result_set:
            # if either of these results has been seen, we need to walk back to previous division
            __, last_operation = operation_list.pop()
            while last_operation == "*2" and len(operation_list)>1 and last_result*2 not in result_set:
                last_result, last_operation = operation_list.pop()
                result_set.remove(last_result)
                last_result, __ = operation_list[-1]
            operation_list.append((last_result*2,"*2"))

# Tried with a different algorithm, but it still fails the following tests:
# FAILED test_ops.py::test_num_ops[15-17] - assert 37 == 17
# FAILED test_ops.py::test_num_ops[55-24] - assert 104 == 24
# FAILED test_ops.py::test_num_ops[102-25] - assert 128 == 25
# FAILED test_ops.py::test_num_ops[1985-42] - assert 2091 == 42
# FAILED test_ops.py::test_num_ops[2020-24] - assert 350 == 24
# FAILED test_ops.py::test_num_ops[3012-22] - assert 1484 == 22

# I suppose the algorithm finds a solution, just not the shortest path

# Brute force approach might not be an option given that some of these examples in the test suite go up to 42 operations
# 2**42 = 4398046511104