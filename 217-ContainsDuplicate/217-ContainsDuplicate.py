# Last updated: 1/29/2026, 12:07:29 AM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7
8        duplicate_finder = set()
9
10        # O(n)
11        for num in nums:
12            if num in duplicate_finder:
13                return True
14            else:
15                duplicate_finder.add(num)
16        
17        # total: O(n)
18        return False
19        