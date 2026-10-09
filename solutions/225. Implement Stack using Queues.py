from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # O(n)
        n = len(self.q)
        self.q.append(x)
        for _ in range(n):
            self.q.append(self.q.popleft()) 
            # queue pop -> popleft, stack pop -> pop()

    def pop(self) -> int:
        # O(1)
        return self.q.popleft()


    def top(self) -> int:
        # O(1)
        return self.q[0]

    def empty(self) -> bool:
        # O(1)
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()