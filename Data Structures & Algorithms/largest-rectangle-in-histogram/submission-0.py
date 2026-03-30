class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxAre = 0
        stack = []
        
        for i , heig in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heig:
                index,height = stack.pop()
                maxAre = max(maxAre , height*(i - index))
                start = index 
            stack.append((start,heig))
        for i, h in stack:
            maxAre = max(maxAre , h*(len(heights)-i))
        return maxAre

        