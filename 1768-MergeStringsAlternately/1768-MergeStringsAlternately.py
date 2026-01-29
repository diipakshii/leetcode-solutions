# Last updated: 1/28/2026, 11:54:26 PM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: str
7        """
8        output = ""
9
10        alt_len = min(len(word1), len(word2)) 
11
12        for i in range(alt_len):
13            output = output + word1[i] + word2[i]
14
15        if len(word1) > len(word2):
16            output = output + word1[alt_len:]
17        else:
18            output = output + word2[alt_len:]
19
20        return output
21        