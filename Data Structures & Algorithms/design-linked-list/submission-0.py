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
        newHead = ListNode(val)
        next, prev = self.head.next, self.head
        next.prev = prev.next = newHead
        newHead.next, newHead.prev = next, prev

    def addAtTail(self, val: int) -> None:
        newTail = ListNode(val)
        next, prev = self.tail, self.tail.prev
        next.prev = prev.next = newTail
        newTail.next, newTail.prev = next, prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur != self.tail:
            if index == 0:
                new = ListNode(val)
                next, prev = cur, cur.prev
                next.prev = prev.next = new
                new.next, new.prev = next, prev
                break
            index -= 1
            cur = cur.next
        if index == 0 and cur == self.tail:
            new = ListNode(val)
            next, prev = cur, cur.prev
            next.prev = prev.next = new
            new.next, new.prev = next, prev


    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur != self.tail:
            if index == 0:
                next, prev = cur.next, cur.prev
                next.prev, prev.next = prev, next
                break
            index -= 1
            cur = cur.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)