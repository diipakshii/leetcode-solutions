# Last updated: 1/29/2026, 3:06:05 PM
1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8
9        # O(1)
10        if len(s) != len(t):
11            return False
12
13        letters = {}
14
15        # O(n)
16        for i in range(len(s)):
17            curr = s[i]
18            if curr in letters:
19                letters[curr] += 1
20            else:
21                letters[curr] = 1
22        
23        # O(n)
24        for j in range(len(t)):
25            curr = t[j]
26            if curr in letters:
27                letters[curr] -= 1
28                if letters[curr] == 0:
29                    letters.pop(curr)
30            else:
31                return False
32        
33        # O(1)
34        if len(letters) > 0:
35            return False
36        
37        # total: O(n)
38        return True
39        