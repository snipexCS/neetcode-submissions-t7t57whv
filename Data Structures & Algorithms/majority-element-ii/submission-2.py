class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cont = Counter(nums)
        res = []
        for num in cont:
            if cont[num] > len(nums)//3:
                res.append(num)
        return res
        