class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        table = [[0]*(n) for _ in range(m)]
        table[0][0] = 1

        if obstacleGrid[0][0] == 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if i+1 < m:
                    if obstacleGrid[i+1][j] == 0:
                        table[i+1][j] += table[i][j]
                    else:
                        table[i+1][j] = 0
                if j+1 <n:
                    if obstacleGrid[i][j+1] == 0:
                        table[i][j+1] += table[i][j]
                    else:
                        table[i][j+1] = 0
                    
                    
        return table[-1][-1]
