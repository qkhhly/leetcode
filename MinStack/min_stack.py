

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.data = []
        self.min = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)

        if len(self.min) == 0:
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)

    # @return nothing
    def pop(self):
        x = self.data.pop()

        if x == self.min[-1]:
            self.min.pop()

    # @return an integer
    def top(self):
        return self.data[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]
        