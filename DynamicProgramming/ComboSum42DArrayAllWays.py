class Solution:
    memo = {}
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

       
        table = [[] for _ in range(target+1)]
        table[0] = [[]]
        
        for i in range(target+1):
            for num in candidates:
                if i+num <= target:

                    next_list = []
                    for arr in table[i]:
                        new_list = arr + [num]
                        new_list.sort()
                        if new_list not in next_list and new_list not in table[i+num]:
                            next_list.append(new_list)
                    table[i+num] += next_list       

        return  table[target]
        
        
                
                
