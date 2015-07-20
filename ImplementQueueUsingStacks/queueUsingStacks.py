class Stack:
    # implement a simple stack class
    def __init__(self):
        self.data = []
    
    def push(self, x):
        # push x to the top (end of the list)
        self.data.append(x)
    
    def peek(self):
        # return the top element
        return self.data[-1]
    
    def pop(self):
        # pop and return the top element
        return self.data.pop()
    
    def size(self):
        return len(self.data)
    
    def empty(self):
        return self.size() == 0

def reverse_stack(stack1, stack2):
    '''reverse stack1 to stack2 by popping elements from stack1 and pushing them to stack2, assuming stack2 is an empty stack'''

    while not stack1.empty():
        stack2.push(stack1.pop())


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.data = Stack()
        self.reverse_data = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.reverse_data.empty() and not self.data.empty():
            reverse_stack(self.data, self.reverse_data)

        self.reverse_data.push(x)

    # @return nothing
    def pop(self):
        if self.data.empty() and not self.reverse_data.empty():
            reverse_stack(self.reverse_data, self.data)

        self.data.pop()

    # @return an integer
    def peek(self):
        if self.data.empty() and not self.reverse_data.empty():
            reverse_stack(self.reverse_data, self.data)

        return self.data.peek()

    # @return an boolean
    def empty(self):
        return self.data.empty() and self.reverse_data.empty()