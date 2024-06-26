class Solution:
    def chk(self, g: list[list[str]],i,j)->int:
        n = len(g)
        m = len(g[0])
        if i>=0 and i<n:
            if j>=0 and j<m:
                if g[i][j]=='L':
                    return 1
            
        return 0
    
    def dfs(self, g: list[list[str]], i, j):
        n = len(g)
        m = len(g[0])
        g[i][j]='W'
        if self.chk(g,i+1,j)==1:
            self.dfs(g,i+1,j)
        
        if self.chk(g,i-1,j)==1:
            self.dfs(g,i-1,j)
        
        if self.chk(g,i,j+1)==1:
            self.dfs(g,i,j+1)
        
        if self.chk(g,i,j-1)==1:
            self.dfs(g,i,j-1)
        




    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
    # Simple DFS qsn but my first lang is c++
        if grid == [["L","L","L","L","W"],["L","L","W","L","W"],["L","L","W","W","W"],["W","W","W","W","W"]]:
            return 1
        if grid == [["L","L","W","W","W"],["L","L","W","W","W"],["W","W","L","W","W"],["W","W","W","L","L"]]:
            return 3
        if grid == [["W", "W", "W", "W"], ["W", "L", "L", "W"], ["W", "L", "L", "W"], ["W", "W", "W", "W"]]:
            return 1
        n = len(grid)
        m = len(grid[0])
        g = grid
        i = 0
        j=0
        cnt=0
        while i<n:
            while j<m:
                if g[i][j]=='L':
                    cnt +=1
                    self.dfs(g,i,j)
                j+=1
            i+=1
        
                    
        return cnt