# Last updated: 8/3/2025, 12:36:16 AM
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0 or not s:
            return 0
            
        left = 0
        curr = {}
        max_len = 0

        for right in range(len(s)):
            if s[right] in curr:
                curr[s[right]] += 1
            else:
                while len(curr) >= k:
                    curr[s[left]] -= 1
                    if curr[s[left]] == 0:
                        del curr[s[left]]
                    left += 1
                curr[s[right]] = 1

            max_len = max(max_len, right - left + 1)
        
        return max_len