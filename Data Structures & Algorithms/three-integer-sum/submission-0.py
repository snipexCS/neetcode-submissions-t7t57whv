class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index , number in enumerate(nums):
            if number > 0 :
                break
            
            if index > 0 and number == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                sums = number + nums[left] + nums[right]

                if sums > 0:
                    right -=1
                elif sums < 0 :
                    left+=1
                else:
                    res.append([number,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        
        return res
        