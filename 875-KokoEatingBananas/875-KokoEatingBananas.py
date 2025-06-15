# Last updated: 6/14/2025, 10:21:15 PM
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        left = 1
        right = max(piles) # upper bound

        while left <= right:
            k = (left + right) // 2

            totalTime = 0

            for i in piles:
                totalTime += math.ceil(float(i) / k)

            if totalTime <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1
        return ans
        