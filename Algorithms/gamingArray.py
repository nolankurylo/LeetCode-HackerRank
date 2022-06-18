
def gamingArray(arr):
    # Write your code here
    num_moves = 0
    max_num = 0
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            num_moves += 1
        
    if num_moves % 2 == 0:
        return "ANDY"
    else:
        return "BOB"

