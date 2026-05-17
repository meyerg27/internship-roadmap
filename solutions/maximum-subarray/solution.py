"""
Maximum Subarray — LeetCode #53
Category: Kadane's Algorithm
Difficulty: Medium

Given an integer array nums, find the subarray with the largest sum and return its sum.

Kadane's Algorithm:
- At each position, decide: start new subarray here, or extend existing?
- max_ending_here = max(nums[i], max_ending_here + nums[i])
- max_so_far = max(max_so_far, max_ending_here)
- Time: O(n), Space: O(1)
"""


def max_subarray(nums: list[int]) -> int:
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# --- Tests ---
assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6,   "Classic: [4,-1,2,1]"
assert max_subarray([1]) == 1,                                       "Single element"
assert max_subarray([5, 4, -1, 7, 8]) == 23,                      "All positive"
assert max_subarray([-1]) == -1,                                     "Single negative"
assert max_subarray([-2, -1]) == -1,                                "Two negatives"
print("All tests passed!")
