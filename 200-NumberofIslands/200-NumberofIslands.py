# Last updated: 8/2/2025, 3:37:05 PM
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        count = 0
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in visited and grid[r][c] == "1":
                visited.add((r,c))

                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1

        return count