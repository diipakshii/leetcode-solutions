# Last updated: 7/17/2025, 1:26:09 AM
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                continue
            else:
                stack.append(portion)
        
        final = "/" + "/".join(stack)

        return final
