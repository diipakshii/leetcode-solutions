# Last updated: 6/13/2025, 11:40:26 AM
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []    

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        # if val is smaller than current min in stack will add, else will keep current min
        self.minStack.append(val)
        # minStack at index i holds min val of stack up to index i
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()