# Last updated: 6/15/2025, 12:06:35 AM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # stack -> O(n) time
        
        result = [0] * len(temperatures)
        
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((t, i))
        return result