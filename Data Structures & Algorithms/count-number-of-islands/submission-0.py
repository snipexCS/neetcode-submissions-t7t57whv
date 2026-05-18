class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    self.dfs(r,c,visited,grid)
                    islands +=1
        return islands
        
    def dfs(self,r,c,visited,grid):
        if r >= len(grid) or c >= len(grid[0]) or r < 0 or c <0:
            return
        if (r,c) in visited or grid[r][c] == "0":
            return
        visited.add((r,c))
        self.dfs(r+1, c, visited, grid)
        self.dfs(r-1, c, visited, grid)
        self.dfs(r, c+1, visited, grid)
        self.dfs(r, c-1, visited, grid)

    
    