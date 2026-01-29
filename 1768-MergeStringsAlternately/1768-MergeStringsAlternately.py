# Last updated: 1/29/2026, 12:01:39 AM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: str
7        """
8
9        output = ""
10
11        curr = 0
12
13        # min function has time complexity of O(n)
14        alt_len = min(len(word1), len(word2))
15
16        while curr < alt_len:
17            output = output + word1[curr] + word2[curr]
18            curr += 1
19
20        if len(word1) > len(word2):
21            # slicing is time complexity of O(k)
22            output = output + word1[alt_len:]
23        else:
24            # slicing is time complexity of O(k)
25            output = output + word2[alt_len:]  
26
27        return output