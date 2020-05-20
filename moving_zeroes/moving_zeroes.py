'''
Input: a List of integers
Returns: a List of integers
'''
# FIRST PASS
def moving_zeroes(arr):
    left_idx = 0
    right_idx = len(arr) - 1

    # make left point to first zero
    while arr[left_idx] != 0 and left_idx != right_idx:
        left_idx += 1

    # make right point to last non-zero
    while arr[right_idx] == 0 and right_idx != left_idx:
        right_idx -= 1

    while left_idx < right_idx:
        if arr[left_idx] == 0 and arr[right_idx] != 0:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
        
        left_idx += 1
        right_idx -= 1
    
    return arr
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")