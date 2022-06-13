class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        table = [[0] * (len(s)) for _ in range(len(s))] 
        for i in range(len(s)):
             table[i][i] = True
        longest_palindrome = s[0]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):

                    
                if s[i] == s[j]:
                    
                    if j-i == 1:
                        table[i][j] = True
                        
                    if table[i+1][j-1]:
                        table[i][j] = True
                        
                    if table[i][j] == True and len(s[i:j+1]) > len(longest_palindrome):
                        longest_palindrome = s[i:j+1]
        return longest_palindrome
                    
                 
                    
            
        
