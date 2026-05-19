class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    max_area = max(max_area,self.dfs(r,c,visited,grid)) 

        return max_area       
    
    def dfs(self,r,c,visited,grid):
        if r < 0 or c < 0 or r >=len(grid) or c >=len(grid[0]):
            return 0 
        
        if (r,c) in visited or grid[r][c] == 0:
            return 0
        
        visited.add((r,c))

        return (1+self.dfs(r+1,c,visited,grid)+self.dfs(r-1,c,visited,grid)+self.dfs(r,c+1,visited,grid)+self.dfs(r,c-1,visited,grid))