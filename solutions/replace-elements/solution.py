"""
Replace Elements with Greatest on the Right — LeetCode #1299
Category: Arrays & Hashing
Difficulty: Easy

Given an array arr, replace every element with the greatest element
among the elements to its right, and replace the last element with -1.

Approach: Right-to-left pass
- Keep track of max seen so far
- Start from right, update max, replace element
- Time: O(n), Space: O(1) in-place
"""


def replace_elements(arr: list[int]) -> list[int]:
    max_so_far = -1

    # Traverse right to left
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = max_so_far
        max_so_far = max(max_so_far, current)

    return arr


# --- Tests ---
assert replace_elements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
assert replace_elements([400]) == [-1]
assert replace_elements([1, 2, 3, 4, 5]) == [5, 5, 5, 5, -1]
print("All tests passed!")
