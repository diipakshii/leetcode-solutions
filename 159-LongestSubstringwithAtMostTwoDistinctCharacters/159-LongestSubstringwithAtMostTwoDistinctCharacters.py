# Last updated: 8/3/2025, 5:06:21 PM
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False
        
        # add similar pairs in a hashmap
        pairs = {}

        for sublist in similarPairs:
            word1, word2 = sublist
            if word1 in pairs:
                pairs[word1].append(word2)
            else:
                pairs[word1] = [word2]
        
        # match up similar pairs
        for i, (word1, word2) in enumerate(zip(sentence1, sentence2)):
            if word1 == word2:
                continue
            if (word1 in pairs and word2 in pairs[word1]) or (word2 in pairs and word1 in pairs[word2]):
                continue
            return False

        return True 
        