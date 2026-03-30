class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        distance = float("inf")
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total>=target:
                distance = min(right - left + 1 , distance)
                total -= nums[left]
                left += 1 

        return 0 if distance == float("inf") else distance

        