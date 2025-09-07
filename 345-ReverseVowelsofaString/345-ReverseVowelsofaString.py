# Last updated: 9/7/2025, 3:15:24 AM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        orig_max = max(candies)

        output = list()

        for i in range(len(candies)):
            if candies[i] + extraCandies >= orig_max:
                output.append(True)
            else:
                output.append(False)
        
        return output
        

        