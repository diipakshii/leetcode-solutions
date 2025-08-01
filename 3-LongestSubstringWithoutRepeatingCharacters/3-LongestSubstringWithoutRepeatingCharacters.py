# Last updated: 7/31/2025, 11:59:06 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)

        if n == 0 or n == 1:
            return n
        
        left = 0
        right = 0

        curr = set()
        max_count = 0
        count = 0

        while right < n:
            if s[right] not in curr:
                curr.add(s[right])
                right += 1
                
                count += 1
                max_count = max(max_count, count)
            else:
                curr.remove(s[left])
                left += 1
                
                count -= 1
        
        return max_count