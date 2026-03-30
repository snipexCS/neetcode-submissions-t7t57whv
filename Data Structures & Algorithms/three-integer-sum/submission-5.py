class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index , num in enumerate(nums):

            if index > 0 and num == nums[index-1]:
                continue
        

            left = index + 1
            right = len(nums) - 1 
            while left < right:
                sumsa = num + nums[left] + nums[right]
                if sumsa > 0 :
                    right-=1
                elif sumsa < 0:
                    left+=1
                else:
                    res.append([num,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left -1] and left < right:
                        left+=1
        
        return res