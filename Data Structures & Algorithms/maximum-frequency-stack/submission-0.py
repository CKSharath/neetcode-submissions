class FreqStack:

    def __init__(self):
        self.cnt={}
        self.m=0
        self.st={}

    def push(self, val: int) -> None:
        valcnt=1+self.cnt.get(val,0)
        self.cnt[val]=valcnt
        if valcnt>self.m:
            self.m=valcnt
            self.st[self.m]=[]
        self.st[valcnt].append(val)

    def pop(self) -> int:
        val=self.st[self.m].pop()
        self.cnt[val]-=1
        if not self.st[self.m]:
            self.m-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()