# Last updated: 6/20/2025, 11:39:11 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # have to reformat dictionary to list for sorting
        
        freq_list = []

        for key, value in freq.items():
            freq_list.append((key, value))

        freq_list.sort(key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(freq_list[i][0])
        
        return result
        