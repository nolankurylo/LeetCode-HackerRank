class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        longest_sequence = 1
        curr_sequence = 1
        
        if len(nums) == 0:
            return 0
        
        for i in range(1, len(nums)):
            prev_num = nums[i-1]
            curr_num = nums[i]
            
            if curr_num == prev_num:
                continue
            
            if curr_num - 1 == prev_num:
                curr_sequence += 1
            else:
                if curr_sequence > longest_sequence:
                    longest_sequence = curr_sequence
                curr_sequence = 1
            
                
            
        if curr_sequence > longest_sequence:
                longest_sequence = curr_sequence
                
        return longest_sequence
    
