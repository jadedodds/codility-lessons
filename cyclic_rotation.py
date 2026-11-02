# Problem: Cyclic Rotation (Arrays)
# Task: Rotate array A to the right by K steps.
# Example: A = [3, 8, 9, 7, 6], K = 3  ->  [9, 7, 6, 3, 8]
# Time complexity: O(N), Space complexity: O(N)
# Sources: Claude (Anthropic) used to review solution, Nov 2, 2026


def solution(A, K):
    # An empty array has nothing to rotate
    if not A:
        return A

    n = len(A)

    # Rotating by n steps gives back the original array,
    # so only the remainder of K divided by n matters
    K = K % n

    # No rotation needed
    if K == 0:
        return A

    # A[-K:] is the last K elements, A[:-K] is everything before them.
    # Putting the last K elements first performs the right rotation.
    return A[-K:] + A[:-K]


# Test cases (expected output in comments)
print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1))        # [0, 0, 0]
print(solution([1, 2, 3, 4], 4))     # [1, 2, 3, 4]
print(solution([], 5))               # []
print(solution([1], 100))            # [1]
