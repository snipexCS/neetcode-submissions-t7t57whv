class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left+=1
                leftMax = max(leftMax , height[left])
                max_water += leftMax - height[left]
            else:
                right-=1
                rightMax = max(rightMax , height[right])
                max_water += rightMax - height[right]
        return max_water

                



        


        