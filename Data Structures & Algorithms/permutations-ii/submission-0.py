class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        perm = []
        visit = [False] * n

        def dfs():
            if len(perm) == n:
                res.append(perm.copy())
                return
            for i in range(n):
                if visit[i]:
                    continue
                if nums[i] == nums[i-1] and i and not  visit[i-1]:
                    continue
                perm.append(nums[i])
                visit[i] = True
                dfs()
                visit[i] = False
                perm.pop()
                  
        nums.sort()
        dfs()
        return res