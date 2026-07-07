# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            
            cur = node
            if node.next:
                cur = dfs(node.next)
                node.next.next = node
            node.next = None
            return cur

        return dfs(head) if head else None