"""
Valid Anagram — LeetCode #242
Category: Arrays & Hashing
Difficulty: Easy

Given two strings s and t, return True if t is an anagram of s, and False otherwise.

An anagram uses all the original characters exactly once, just rearranged.

Approach: Character count hash map
- Count frequency of each char in s
- Decrement for each char in t
- All counts must be zero for valid anagram
- Time: O(n), Space: O(1) — alphabet is fixed size (26)
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # Fixed alphabet size
    a_ord = ord('a')

    for c in s:
        count[ord(c) - a_ord] += 1
    for c in t:
        idx = ord(c) - a_ord
        count[idx] -= 1
        if count[idx] < 0:
            return False

    return True


# --- Tests ---
assert is_anagram("anagram", "nagaram") == True,  "Basic anagram"
assert is_anagram("rat", "car") == False,          "Not an anagram"
assert is_anagram("listen", "silent") == True,     "listen/silent"
assert is_anagram("a", "a") == True,               "Single char"
assert is_anagram("a", "b") == False,              "Different chars"
assert is_anagram("abc", "abcd") == False,          "Different lengths"
print("All tests passed!")
