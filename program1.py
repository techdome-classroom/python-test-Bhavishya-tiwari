class Solution:
    def check(g,i,j):
        n = len(g)
        m = len(g[0])
        if i>=0 and i<n:
            if j>=0 and j<m:
                return 1
            
        return 0
    
    def dfs(g, i, j):
        n = len(g)
        m = len(g[0])
        g[i][j]='o'
        if check(g,i+1,j)==1:
            



    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
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
                    dfs(g,i,j)
                    
        return 0