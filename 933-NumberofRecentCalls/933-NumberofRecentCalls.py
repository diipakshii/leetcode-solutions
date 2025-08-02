# Last updated: 8/2/2025, 12:26:16 AM
class RecentCounter(object):

    def __init__(self):
        self.queue = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()
        
        return len(self.queue)



        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)