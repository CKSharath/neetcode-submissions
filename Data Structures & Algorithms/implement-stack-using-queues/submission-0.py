class MyStack:

    def __init__(self):
        self.q=deque()
        self.q2=deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q:
            self.q2.append(self.q.popleft())
        self.q = self.q2
        self.q2 = deque()

    def pop(self) -> int:
        if self.q:
            return self.q.popleft()

    def top(self) -> int:
        if self.q:
            return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()