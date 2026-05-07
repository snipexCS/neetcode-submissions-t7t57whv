class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 

        while left < right:
            sumsa = numbers[left] + numbers[right]
            if sumsa == target:
                return [left+1,right+1]
            elif sumsa < target:
                left += 1
            elif sumsa > target:
                right-=1
        return -1

        