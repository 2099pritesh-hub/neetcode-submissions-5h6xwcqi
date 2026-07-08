class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur != self.tail:
            if index == 0:
                return cur.val
            index -= 1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        self.insert(self.head, self.head.next, ListNode(val))

    def addAtTail(self, val: int) -> None:
        self.insert(self.tail.prev, self.tail, ListNode(val))

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur != self.tail and index > 0:
            index -= 1
            cur = cur.next
        if index == 0:
            self.insert(cur.prev, cur, ListNode(val))

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur != self.tail:
            if index == 0:
                self.remove(cur)
                break
            index -= 1
            cur = cur.next

    def insert(self, prev, next, node):
        next.prev = prev.next = node
        node.next, node.prev = next, prev

    def remove(self, node):
        next, prev = node.next, node.prev
        next.prev, prev.next = prev, next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)