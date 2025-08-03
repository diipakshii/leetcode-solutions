# Last updated: 8/3/2025, 12:18:23 AM
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        right = 0
        
        max_len = 0
        count = {}

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len