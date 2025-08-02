# Last updated: 8/2/2025, 12:45:17 AM
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)

        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()

            # Whoever comes earlier bans the other
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)

        return "Radiant" if radiant else "Dire"