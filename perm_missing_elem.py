# Problem: Perm Missing Elem (Time Complexity)
# Task: A contains N distinct integers from 1 to N+1, so one is missing.
#       Return the missing integer.
# Example: A = [2, 3, 1, 5]  ->  4
# Time complexity: O(N), Space complexity: O(1)
# Sources: Claude (Anthropic) used for help with the solution, Nov 2, 2026


def solution(A):
    n = len(A)

    # Sum of every number from 1 to n + 1, using the formula k(k+1)/2
    # with k = n + 1. Integer division (//) keeps the result an int.
    expected_sum = (n + 1) * (n + 2) // 2

    # Sum of the numbers actually present in the array
    actual_sum = sum(A)

    # The gap between the two sums is the missing number
    return expected_sum - actual_sum


# Test cases (expected output in comments)
print(solution([2, 3, 1, 5]))  # 4
print(solution([]))            # 1 (range is just 1, and it is missing)
print(solution([2]))           # 1
print(solution([1]))           # 2
print(solution([1, 2, 3]))     # 4 (the last number is missing)
