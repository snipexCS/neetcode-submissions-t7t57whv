class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        maxArea = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    maxArea = max(maxArea,self.search(grid,i,j,visited))
        
        return maxArea
        

    def search(self,grid,i,j,visited):
        if i < 0 or i >= len(grid)or j < 0 or j >= len(grid[0]):
            return 0 
            
        if ((i,j) in visited or grid[i][j] == 0) :
            return 0
        visited.add((i,j))
        return(1+self.search(grid,i+1,j,visited)+self.search(grid,i-1,j,visited)+self.search(grid,i,j+1,visited)+self.search(grid,i,j-1,visited))
            
            

        
        