class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
     
        left, right = 0, len(height)-1
        
        while(1):
              
            max_amount = max(max_amount, min(height[left], height[right]) * abs(left-right))
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
            
            if left >= right:
                    break
                    
        return max_amount
            
            
