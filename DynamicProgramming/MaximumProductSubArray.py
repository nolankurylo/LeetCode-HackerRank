class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product = max(nums)
        curr_min, curr_max = 1, 1
        
        for i in range(len(nums)):
            
            curr_product = curr_max * nums[i]
            curr_max = max(curr_max * nums[i], curr_min * nums[i], nums[i]) 
            curr_min = min(curr_product, curr_min * nums[i], nums[i])
            max_product = max(curr_max, max_product)
        return max_product
    
