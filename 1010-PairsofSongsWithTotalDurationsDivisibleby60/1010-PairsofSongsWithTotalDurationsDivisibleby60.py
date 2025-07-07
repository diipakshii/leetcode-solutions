# Last updated: 7/6/2025, 11:54:49 PM
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # brute force -> O(n^2)
        # hashmap -> O(n)

        # dictionary to hold remainders for each time
        remainders = {}
        count = 0

        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60 

            if complement in remainders:
                count += remainders[complement]

            if remainder in remainders:
                remainders[remainder] += 1
            else:
                remainders[remainder] = 1

        return count