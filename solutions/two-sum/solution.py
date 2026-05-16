"""
Two Sum — LeetCode #1
Category: Arrays & Hashing
Difficulty: Easy

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.

Approach: Hash map (one-pass)
- For each number, compute complement = target - num
- If complement exists in map, we found our pair
- Otherwise, store num -> index in map
- Time: O(n), Space: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # val -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# --- Tests ---
assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Basic case"
assert two_sum([3, 2, 4], 6) == [1, 2], "Non-adjacent pair"
assert two_sum([3, 3], 6) == [0, 1], "Duplicate values"
assert two_sum([1, 5, 3, 7], 8) == [1, 2] or two_sum([1, 5, 3, 7], 8) == [0, 3], "Multiple valid pairs"
print("All tests passed!")
