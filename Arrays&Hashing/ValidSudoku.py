class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if len(board) != 9 or len(board[:]) != 9:
            return False
        
        cols = {}
        rows = {}
        squares = {}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                    
                if j not in cols:
                    cols[j] = []
                if i not in rows:
                    rows[i] = []
                if f'{i//3}{j//3}' not in squares:
                    squares[f'{i//3}{j//3}'] = []
                    
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in squares[f'{i//3}{j//3}']:
                    return False
                
                
               
                cols[j].append(board[i][j])
                rows[i].append(board[i][j])
                squares[f'{i//3}{j//3}'].append(board[i][j])
                           
        return True
                        
