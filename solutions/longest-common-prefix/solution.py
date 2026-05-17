"""
Longest Common Prefix — LeetCode #14
Category: Strings
Difficulty: Easy

Write a function to find the longest common prefix string among an array of strings.
If there is no common prefix, return "".

Approach: Horizontal scanning
- Start with first string as prefix
- Compare with each subsequent string, shrink prefix
- Time: O(S), Space: O(1) where S = sum of all characters
"""


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        # Shrink prefix until it matches start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


# --- Tests ---
assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
assert longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"
assert longest_common_prefix(["a"]) == "a"
assert longest_common_prefix(["a", "a"]) == "a"
assert longest_common_prefix([]) == ""
print("All tests passed!")
