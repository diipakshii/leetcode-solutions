# Last updated: 8/2/2025, 4:47:00 PM
class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # initialize data structure
        self.queue = deque()
        self.dictionary = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        while self.queue and self.dictionary[self.queue[0]] > 1:
            self.queue.popleft()
        
        return self.queue[0] if self.queue else -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        
        if value not in self.dictionary:
            self.queue.append(value)
            self.dictionary[value] = 1
        else:
            self.dictionary[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)