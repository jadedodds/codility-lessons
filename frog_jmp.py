# Problem: Frog Jmp (Time Complexity)
# Task: A frog starts at X and jumps D units each time.
#       Return the minimum number of jumps to reach Y or beyond.
# Example: X = 10, Y = 85, D = 30  ->  3
# Time complexity: O(1), Space complexity: O(1)
# Sources: Claude (Anthropic) used to review solution, Nov 2, 2026


def solution(X, Y, D):
    # Total distance the frog still has to cover
    distance = Y - X

    # Integer ceiling division: adding (D - 1) before dividing
    # rounds up without needing floating-point numbers
    return (distance + D - 1) // D


# Test cases (expected output in comments)
print(solution(10, 85, 30))  # 3
print(solution(10, 10, 30))  # 0 (already at the target)
print(solution(1, 10, 3))    # 3 (distance 9 divides evenly)
print(solution(1, 11, 3))    # 4 (distance 10 needs a partial extra jump)
