# Last updated: 6/20/2025, 11:36:14 PM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # automatically creates an empty list for any new ke
        ans = defaultdict(list)

        for s in strs:
            # sort the string alphabetically
            sorted_str = ''.join(sorted(s))
            # use the sorted string as a key in the dictionary
            ans[sorted_str].append(s)
        
        return list(ans.values())
        