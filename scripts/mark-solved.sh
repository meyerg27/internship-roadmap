#!/bin/bash
#────────────────────────────────────────────
# Mark LeetCode Problem as Solved
# Usage: ./mark-solved.sh <problem_number>
# Example: ./mark-solved.sh 1
#────────────────────────────────────────────

set -e

PROBLEM="${1:-}"

if [[ -z "$PROBLEM" ]]; then
  echo "Usage: $0 <problem_number>"
  exit 1
fi

TODAY=$(date +%Y-%m-%d)
TRACKER="/root/.openclaw/workspace/projects/internship-roadmap/tracking/leetcode-tracker.md"

echo "Marking problem #$PROBLEM as solved on $TODAY..."

# Read the tracker and mark the problem
if [[ -f "$TRACKER" ]]; then
  # Simple sed replacement for the table
  sed -i "s/| $PROBLEM | /| $PROBLEM | ✅ |/" "$TRACKER"
  echo "Updated tracker: $TRACKER"
else
  echo "Tracker not found: $TRACKER"
fi

# Also update the daily log
WEEKLY_DIR="/root/.openclaw/workspace/projects/internship-roadmap/weekly"
CURRENT_WEEK=$(date +W%V).md

if [[ -f "$WEEKLY_DIR/$CURRENT_WEEK" ]]; then
  echo "Problem #$PROBLEM solved on $TODAY" >> "$WEEKLY_DIR/$CURRENT_WEEK"
  echo "Updated weekly log: $WEEKLY_DIR/$CURRENT_WEEK"
fi

echo ""
echo "Don't forget to:"
echo "1. Add solution code to: solutions/$PROBLEM/"
echo "2. Push to GitHub"
