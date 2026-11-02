def solution(A, K):
    # Empty array: nothing to rotate
    if not A:
        return A

    n = len(A)

    # Rotating by n gives the same array, so only the remainder matters
    K = K % n

    # Last K elements move to the front; the rest follow
    # (when K == 0, A[-0:] is the whole array and A[:n] is the whole array,
    # so handle it explicitly)
    if K == 0:
        return A
    return A[-K:] + A[:-K]


# Quick tests
print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1))        # [0, 0, 0]
print(solution([1, 2, 3, 4], 4))     # [1, 2, 3, 4]
print(solution([], 5))               # []
