class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0 
        left = 0
        right = len(heights) - 1 

        while left < right:
            local_area = abs(right-left) * min(heights[left],heights[right])
            max_water = max(max_water,local_area)
            if heights[left] < heights[right]:
                left+=1
            elif heights[right] <= heights[left]:
                right-=1
        
        return max_water




        