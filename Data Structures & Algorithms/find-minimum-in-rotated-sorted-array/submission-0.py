class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left < right:
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                right-=1
            elif nums[right] < nums[left]:
                res =  min(res,nums[right])
                left+=1
        return res

        