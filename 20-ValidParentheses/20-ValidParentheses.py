# Last updated: 6/13/2025, 11:40:31 AM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if char == ")" and last != "(":
                    return False
                if char == "}" and last != "{":
                    return False
                if char == "]" and last != "[":
                    return False
        
        if len(stack) != 0:
            return False
        
        return True