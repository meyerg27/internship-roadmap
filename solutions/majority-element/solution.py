"""
Majority Element — LeetCode #169
Category: Boyer-Moore Voting Algorithm
Difficulty: Easy

Given an array of size n, find the majority element.
The majority element appears more than ⌊n/2⌋ times.
Assume a majority always exists.

Approach: Boyer-Moore Voting Algorithm
- If we pair up all elements that are different,
  the majority element will always survive
- Count tracks current candidate's "votes"
- When count=0, we pick a new candidate
- Time: O(n), Space: O(1)
"""


def majority_element(nums: list[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


# --- Tests ---
assert majority_element([3, 2, 3]) == 3
assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
assert majority_element([1]) == 1
assert majority_element([1, 2, 1]) == 1
assert majority_element([6, 5, 5]) == 5
print("All tests passed!")
