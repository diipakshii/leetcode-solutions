# Last updated: 7/13/2025, 1:27:18 PM
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        # Check if lengths of pattern and words match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                if word in word_to_char:
                    return False
                char_to_word[char] = word
                word_to_char[word] = char

        return True
            

        