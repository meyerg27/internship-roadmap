"""
Reverse Linked List — LeetCode #206
Category: Linked List
Difficulty: Easy

Given the head of a singly linked list, reverse the list and return the reversed list.

Approach 1: Iterative (three pointers)
- prev, current, next
- At each step: save next, reverse pointer, advance
- Time: O(n), Space: O(1)

Approach 2: Recursive
- Base: empty or single node
- Recurse to end, then reverse the last link
- Time: O(n), Space: O(n) call stack
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        node = self
        while node:
            vals.append(str(node.val))
            node = node.next
        return " -> ".join(vals)


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    current = head
    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse link
        prev = current            # Advance prev
        current = next_node      # Advance current
    return prev  # prev is now the new head


def list_to_linked(vals: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    for v in vals:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


# --- Tests ---
assert str(reverse_list(list_to_linked([1, 2, 3, 4, 5]))) == "5 -> 4 -> 3 -> 2 -> 1"
assert str(reverse_list(list_to_linked([1, 2]))) == "2 -> 1"
assert str(reverse_list(list_to_linked([]))) == "None"
assert str(reverse_list(list_to_linked([1]))) == "1"
print("All tests passed!")
