class Solution:
    def check(g,i,j):
        n = len(grid)
        m = len(grid[0])

    def dfs(g, i, j):
        n = len(grid)
        m = len(grid[0])
        g[i][j]='o'



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