# Memoization
class Solution:
    memo = {}
    def uniquePaths(self, m: int, n: int) -> int:
        
        if (m,n) in self.memo: return self.memo[(m,n)]
        if m==1 and n==1: return 1
        if m==0 or n==0: return 0
        self.memo[(m,n)] = self.uniquePaths(m-1,n) + self.uniquePaths(m, n-1)
        return self.memo[(m,n)]
    
 # Tabulation
 class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0]*(n+1) for _ in range(m+1)]
        table[1][1] = 1
        
        for i in range(m+1):
            for j in range(n+1):
                if i+1 <= m:
                    table[i+1][j] += table[i][j]
                if j+1 <=n:
                    table[i][j+1] += table[i][j]
                    
                    
        return table[m][n]
    
    
