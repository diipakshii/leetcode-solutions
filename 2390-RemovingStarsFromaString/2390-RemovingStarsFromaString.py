# Last updated: 7/17/2025, 1:20:05 AM
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if char == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        ans = "".join(stack)

        return ans
            
        