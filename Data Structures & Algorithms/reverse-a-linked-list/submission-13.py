# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            cur = node
            if node.next:
                cur = reverse(node.next)
                node.next.next = node
            node.next = None
            return cur
        return reverse(head) if head else None