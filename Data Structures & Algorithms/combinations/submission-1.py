class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(i,n+1):
                comb.append(i)
                dfs(i+1,comb)
                comb.pop()
            






        dfs(1,[])
        return res
        