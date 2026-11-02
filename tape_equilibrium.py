# Problem: Tape Equilibrium (Time Complexity)
# Task: Split A into two non-empty parts and return the minimum
#       absolute difference between the left sum and the right sum.
# Example: A = [3, 1, 2, 4, 3]  ->  1
# Time complexity: O(N), Space complexity: O(1)
# Sources: Claude (Anthropic) used to review solution, Nov 2, 2026


def solution(A):
    # Sum of the whole array, computed once
    total = sum(A)

    left_sum = 0
    min_diff = float("inf")

    # Stop before the last element so the right part is never empty
    for i in range(len(A) - 1):
        # Move one more element into the left part
        left_sum += A[i]

        # Everything not in the left part is in the right part
        right_sum = total - left_sum

        # Track the smallest difference found so far
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff

    return min_diff


# Test cases (expected output in comments)
print(solution([3, 1, 2, 4, 3]))  # 1
print(solution([1, 1]))           # 0
print(solution([-1000, 1000]))    # 2000
print(solution([5, 5, 5, 5]))     # 0
