class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for index,num in enumerate(nums):
            diff = target - num
            if diff in counter:
                return [counter[diff],index]
            counter[num] = index
        
        