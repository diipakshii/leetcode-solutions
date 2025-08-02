# Last updated: 8/2/2025, 4:28:20 PM
class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.queue = deque()
        self.size = size
        self.total = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) >= self.size:
            self.total -= self.queue.popleft()
        
        self.queue.append(val)
        self.total += val
        return float(self.total) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)