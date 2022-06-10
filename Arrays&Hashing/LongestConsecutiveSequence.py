class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        longest_sequence = 0
        curr_sequence = 
        
        
        for i in range(1, len(nums)+1):
            prev_num = nums[i-1]
            curr_num = nums[i]
            
            if curr_num - 1 == prev_num:
                curr_sequence +=1
            else:
                if curr_sequence > longest_sequence:
                    longest_sequence = curr_sequence
            
                
            
        if curr_sequence > longest_sequence:
                longest_sequence = curr_sequence
                
        return longest_sequence
    
