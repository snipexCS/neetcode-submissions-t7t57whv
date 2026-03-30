class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1 
        
        arr = []
        for key,char in counter.items():
            arr.append((char,key))

        arr.sort()
        res = []

        while k > 0:
            res.append(arr.pop()[1])
            k -= 1
        return res

            