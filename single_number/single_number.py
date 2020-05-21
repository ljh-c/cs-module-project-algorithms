'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# FIRST PASS
def single_number(arr):
    # we need a way to record numbers we have seen
    # we will use a set
    seen = set()

    for num in arr:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    
    (unique,) = seen
    return unique
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")