class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        res = 0 


        while left<=right:
            local_time = 0 
            midSpeed = (left + right) // 2
            for p in piles:
                local_time += math.ceil(p / midSpeed)
            if local_time <= h:
                res = midSpeed
                right = midSpeed - 1
            else:
                left = midSpeed + 1
        
        return res


                



        