class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            
            for index , num in enumerate(trip):
                if num == target[index]:
                    good.add(index)
                    
            
        return len(good) == 3