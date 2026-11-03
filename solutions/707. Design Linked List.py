class Node:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size-index:
            curr = self.head
            for _ in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size-index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        pred = self.head
        succ = self.head.next
        self.size += 1
        new = Node(val)
        new.prev = pred
        new.next = succ
        pred.next = succ
        pred.next = new
        succ.prev = new

    def addAtTail(self, val: int) -> None:
        pred = self.tail.prev
        succ = self.tail
        self.size += 1
        new = Node(val)
        new.prev = pred
        new.next = succ
        pred.next = succ
        pred.next = new
        succ.prev = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index + 1 < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size-index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1
        new = Node(val)
        new.prev = pred
        new.next = succ
        pred.next = succ
        pred.next = new
        succ.prev = new

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        pred = curr.prev
        succ = curr.next
        
        pred.next = succ
        succ.prev = pred

        self.size -= 1
        return curr.val

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)