'''
Input: an integer
Returns: an integer
'''
# FIRST PASS
def eating_cookies(n):
    if n <= 1:
        return 1

    if n == 2:
        return 2

    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
# TIME COMPLEXITY: O(3^n) ?
# SPACE COMPLEXITY: O(1)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
