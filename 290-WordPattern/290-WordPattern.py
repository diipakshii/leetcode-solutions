# Last updated: 7/14/2025, 8:52:06 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_len = 0
        
        hashmap = set(nums)

        for num in hashmap:
            if num - 1 not in hashmap:
                curr = num
                len = 1

                while curr + 1 in hashmap:
                    curr += 1
                    len += 1
                
                max_len = max(max_len, len)
        
        return max_len

            
        