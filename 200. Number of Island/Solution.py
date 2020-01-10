class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:   
        r=len(grid)
        
        c =len(grid[0]) if r else 0
        
        res=0
    
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    res+=1
                    self.DFS(grid,i,j,r,c)
                    
        return res 
        
    def DFS(self,grid,i,j,r,c):
        if i < 0 or j < 0 or i == r or j == c or grid[i][j] != "1":
                return None
        grid[i][j]='0'
        if i-1>=0 and grid [i-1][j]=='1':
            self.DFS(grid,i-1,j,r,c)    
        if i+1<r  and grid [i+1][j]=='1':
            self.DFS(grid,i+1,j,r,c) 
        if j-1>=0 and grid [i][j-1]=='1':
            self.DFS(grid,i,j-1,r,c)
        if j+1<c and grid [i][j+1]=='1':
            self.DFS(grid,i,j+1,r,c)
        
                  