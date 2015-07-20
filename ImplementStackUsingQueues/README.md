# Implement a stack using a queue operations
Here I make use of Python's deque data structure, which has approximately O(1) complexity in pop/push operations on both ends. 

Only a queue's operations are used to implement the stack:
    * push to the right end
    * pop from the left end

Cycle the elements to get the last pushed element when poping from the stack.