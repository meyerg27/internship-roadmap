"""
Contains Duplicate — LeetCode #217
Category: Arrays & Hashing
Difficulty: Easy

Given an integer array nums, return True if any value appears at least twice.

Approach: Hash set
- Add each number to set as we go
- If number already in set → duplicate found
- Time: O(n), Space: O(n)
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# --- Tests ---
assert contains_duplicate([1, 2, 3, 1]) == True,  "Has duplicate"
assert contains_duplicate([1, 2, 3, 4]) == False, "All unique"
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, -2, 4]) == True, "Multiple dupes"
assert contains_duplicate([1, 2, 3, 4, 5]) == False, "Consecutive unique"
print("All tests passed!")
