
from collections import deque


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.data = deque()
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)

    def expose_head(self):
        # cycle the elements to expose the last pushed element to the left
        counter = len(self.data)

        while counter > 1:
            self.data.append(self.data.popleft())
            counter -= 1

    # @return nothing
    def pop(self):
        # cycle the elements to get the last pushed element
        self.expose_head()
        self.data.popleft()

    # @return an integer
    def top(self):
        self.expose_head()
        x = self.data.popleft()
        self.data.append(x)
        return x

    # @return an boolean
    def empty(self):
        return len(self.data) == 0
        