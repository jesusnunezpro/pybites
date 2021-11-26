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
    operations = 0
    current_value = 1

    while (not current_value == n) and (operations < 100):
        if n % 2:
            current_value = current_value*2 if current_value < n*3 else current_value//3
        else:
            current_value = current_value*2 if current_value < n else current_value//3
        operations += 1

    return operations

# This algorithm just doesn't pass the tests, all failed tests got return values of 100
# test_ops.py::test_num_ops[10-6] PASSED    
# test_ops.py::test_num_ops[12-9] PASSED     
# test_ops.py::test_num_ops[15-17] FAILED   
# test_ops.py::test_num_ops[33-18] FAILED    
# test_ops.py::test_num_ops[55-24] FAILED    
# test_ops.py::test_num_ops[102-25] FAILED   
# test_ops.py::test_num_ops[1985-42] FAILED 
# test_ops.py::test_num_ops[2020-24] FAILED  
# test_ops.py::test_num_ops[3012-22] FAILED
