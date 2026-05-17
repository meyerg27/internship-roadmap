"""
Is Subsequence — LeetCode #392
Category: Two Pointers
Difficulty: Easy

Given two strings s and t, return True if s is a subsequence of t.

A subsequence is a sequence that can be derived from another sequence
by deleting some or no characters without changing the order.

Approach: Two pointers
- s pointer at start, t pointer at start
- Advance t pointer until chars match
- If we finish s → all chars found → True
- If we finish t before s → missing chars → False
- Time: O(n), Space: O(1)
"""


def is_subsequence(s: str, t: str) -> bool:
    s_ptr = 0
    for t_ptr in range(len(t)):
        if s_ptr >= len(s):
            break
        if t[t_ptr] == s[s_ptr]:
            s_ptr += 1
    return s_ptr == len(s)


# --- Tests ---
assert is_subsequence("abc", "ahbgdc") == True,   "abc in ahbgdc"
assert is_subsequence("axc", "ahbgdc") == False,  "axc NOT in ahbgdc"
assert is_subsequence("", "ahbgdc") == True,       "Empty s is always subsequence"
assert is_subsequence("abc", "") == False,        "Non-empty s, empty t"
assert is_subsequence("", "") == True,              "Both empty"
assert is_subsequence("b", "abc") == True,         "Single char"
print("All tests passed!")
