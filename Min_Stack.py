class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.value = []
        self.min = math.inf
        self.topv = [[],[]]

    def push(self, x: int) -> None:
        if x < self.min:
            self.min= x
        self.topv = [x,self.min]
        self.value.append(self.topv)

    def pop(self) -> None:
    
        self.value.pop()
        if len(self.value) > 0:
            self.topv = self.value[-1]
            self.min = self.topv[1]
        else:
            self.topv = [[],[]]
            self.min = math.inf
    def top(self) -> int:
        return self.topv[0]

    def getMin(self) -> int:
        return self.topv[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()