# Last updated: 7/18/2025, 12:44:10 AM
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curString = ""

        for char in s:
            if char == "[":
                stack.append(curString)
                stack.append(curNum)
                # reset
                curString = ""
                curNum = 0
            elif char == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif char.isdigit():
                curNum = curNum * 10 + int(char)
            else:
                curString += char
        
        return curString
     