'''class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = 0
        l,r = 0 , len(heights)-1
        while l<r:
            current= min(heights[l], heights[r]) * (r-l)
            high = max(current,high)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-1
        return high'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        high = 0
        
        while l < r:
            # Calculate current area
            current = min(heights[l], heights[r]) * (r - l)
            high = max(high, current)
            
            # Move the pointer at the shorter line
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return high
