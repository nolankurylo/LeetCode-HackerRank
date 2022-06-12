

def flippingMatrix(matrix):
    n = len(matrix) 
    maximal_sum = 0
    for i in range(n //2):
        for j in range(n //2):
            maximal_sum += max(matrix[i][j], matrix[-1-i][j], matrix[i][-1-j],matrix[-1-i][-1-j] )
        
    return maximal_sum
        
        

