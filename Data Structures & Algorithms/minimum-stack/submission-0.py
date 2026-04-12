class MinStack:

    def __init__(self):
        # initialize main stack and min stack
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        # push value to main stack
        self.stack.append(val)
        # push to minstack if empty or value is smaller or equal than top of minstack
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)
        # else if not smaller duplicate top of minstack
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        # remove the element from the top of both stacks
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        # retrieve the top element
        return self.stack[-1]
        

    def getMin(self) -> int:
        # get the last value in min stack
        return self.minStack[-1]
        
