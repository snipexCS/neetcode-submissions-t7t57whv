class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numset:
                local_longest = 1 
            
                while num + local_longest in numset:
                    local_longest+=1
                longest = max(longest , local_longest)
        
        return longest