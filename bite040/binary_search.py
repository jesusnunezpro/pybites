def binary_search(sequence, target):
    start = 0
    end = len(sequence)
    halfway_point = int(end/2)
    while sequence[halfway_point] != target and end-start > 1:
        if sequence[halfway_point] > target:
            end = halfway_point
        elif sequence[halfway_point] < target:
            start = halfway_point
        else:
            break
        halfway_point = int((end+start)/2)
        print(f"halfway_point = {halfway_point} current = {sequence[halfway_point]}")
    
    return halfway_point if sequence[halfway_point] == target else None
