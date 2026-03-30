class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index,temp in enumerate(temperatures):
            while stack and  temp > stack[-1][0]:
                stackTemp , stackIndx = stack.pop()
                result[stackIndx] = index - stackIndx
            
            stack.append((temp,index))
        
        return result
            
            
        