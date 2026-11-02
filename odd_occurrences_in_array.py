# Problem: Odd Occurrences in Array (Arrays)
# Task: Every value in A appears an even number of times except one.
#       Return the value that has no pair.
# Example: A = [9, 3, 9, 3, 9, 7, 9]  ->  7
# Time complexity: O(N), Space complexity: O(1)
# Sources: Claude (Anthropic) used for help with the solution, Nov 2, 2026


def solution(A):
    # XOR of a number with itself is 0, and XOR with 0 leaves a number unchanged
    result = 0

    # XOR every number together: each pair cancels out,
    # so only the unpaired value remains
    for number in A:
        result ^= number

    return result


# Test cases (expected output in comments)
print(solution([9, 3, 9, 3, 9, 7, 9]))  # 7
print(solution([42]))                    # 42
print(solution([1, 1, 2]))               # 2
print(solution([4, 5, 4, 6, 5]))         # 6
