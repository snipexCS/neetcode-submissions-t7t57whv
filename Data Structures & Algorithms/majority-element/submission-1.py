class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxcounter = 0 
        result = 0

        for num in nums:
            count[num] +=1
            if maxcounter < count[num]:
                res = num
                maxcounter = count[num]
                
        return res


        