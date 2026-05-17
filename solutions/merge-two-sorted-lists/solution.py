"""
Merge Two Sorted Lists — LeetCode #21
Category: Linked List
Difficulty: Easy

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list and return the head of the merged linked list.

Approach: Dummy head + pointer iteration
- Use a dummy head to simplify edge cases
- Compare nodes from both lists, attach smaller one
- When one list is exhausted, attach remaining list
- Time: O(n + m), Space: O(1) — we just relink pointers
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


def merge_two_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach whatever remains
    current.next = l1 or l2
    return dummy.next


def list_to_linked(vals: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    for v in vals:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


# --- Tests ---
assert str(merge_two_lists(list_to_linked([1,2,4]), list_to_linked([1,3,4]))) == "1 -> 1 -> 2 -> 3 -> 4 -> 4"
assert str(merge_two_lists(list_to_linked([]), list_to_linked([]))) == "None"
assert str(merge_two_lists(list_to_linked([]), list_to_linked([0]))) == "0"
assert str(merge_two_lists(list_to_linked([1,3,5]), list_to_linked([2,4,6]))) == "1 -> 2 -> 3 -> 4 -> 5 -> 6"
print("All tests passed!")
