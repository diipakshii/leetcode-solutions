# Last updated: 7/5/2025, 1:46:03 PM
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # hashmap 
        # count number of 5s, 10s, and 20s

        counts = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                counts[5] += 1
            elif bill == 10:
                if counts[5] == 0:
                    return False
                counts[5] -= 1
                counts[10] += 1
            elif bill == 20:
                if counts[10] > 0 and counts[5] > 0:
                    counts[10] -= 1
                    counts[5] -= 1
                elif counts[5] >= 3:
                    counts[5] -= 3
                else:
                    return False

        return True