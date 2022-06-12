class Solution:
    memo = {}
    
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = {}
        self.sumMe(nums, target)
        return self.memo[target]
       
        

    def sumMe(self, nums: List[int], target: int) -> list:
        if target in self.memo: return self.memo[target]
        if target == 0: return 1
        if target < 0: return 0
        
        total_ways = 0
        
        for num in nums:
            remainder = target - num
            numWaysForRest = self.sumMe(nums, remainder)
            total_ways += numWaysForRest 
               
        self.memo[target] = total_ways
        return total_ways
