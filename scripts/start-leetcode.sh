#!/bin/bash
#────────────────────────────────────────────
# LeetCode Problem Runner
# Usage: ./solve.sh <problem_number>
# Example: ./solve.sh 1  → opens Two Sum
#────────────────────────────────────────────

set -e

PROBLEM="${1:-}"

if [[ -z "$PROBLEM" ]]; then
  echo "Usage: $0 <problem_number>"
  echo ""
  echo "NeetCode 150 Problems:"
  echo "  1  - Two Sum (Easy)"
  echo "  2  - Valid Anagram (Easy)"
  echo "  3  - Contains Duplicate (Easy)"
  echo "  4  - Replace Elements with Greatest (Easy)"
  echo "  5  - Is Subsequence (Easy)"
  echo "  6  - Longest Common Prefix (Easy)"
  echo "  7  - Merge Two Sorted Lists (Easy)"
  echo "  8  - Maximum Subarray (Easy)"
  echo "  9  - Best Time to Buy Stock (Easy)"
  echo "  10 - Maximum Depth of Binary Tree (Easy)"
  exit 1
fi

declare -A PROBLEMS
PROBLEMS=(
  [1]="two-sum"
  [2]="valid-anagram"
  [3]="contains-duplicate"
  [4]="replace-elements-with-greatest-element-on-right"
  [5]="is-subsequence"
  [6]="longest-common-prefix"
  [7]="merge-two-sorted-lists"
  [8]="maximum-subarray"
  [9]="best-time-to-buy-and-sell-stock"
  [10]="maximum-depth-of-binary-tree"
)

PROBLEM_SLUG="${PROBLEMS[$PROBLEM]:-}"

if [[ -z "$PROBLEM_SLUG" ]]; then
  echo "Problem $PROBLEM not found in NeetCode 150 list"
  exit 1
fi

echo "=== LeetCode Problem #$PROBLEM ==="
echo "Slug: $PROBLEM_SLUG"
echo "URL: https://leetcode.com/problems/$PROBLEM_SLUG/"
echo ""

# Try to open in browser
if command -v open &>/dev/null; then
  open "https://leetcode.com/problems/$PROBLEM_SLUG/"
elif command -v xdg-open &>/dev/null; then
  xdg-open "https://leetcode.com/problems/$PROBLEM_SLUG/"
fi

# Check if leetcode-cli is available
if command -v lc &>/dev/null; then
  echo "Opening with leetcode-cli..."
  lc shell "$PROBLEM_SLUG"
elif command -v leetcode &>/dev/null; then
  echo "Opening with leetcode..."
  leetcode problems -t "$PROBLEM_SLUG"
fi

echo ""
echo "After solving, run: ./mark-solved.sh $PROBLEM"
