class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 !=0:
            return False
        
        length = total_length // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(start):
            if start == len(matchsticks):
                return True
            
            for side in range(4):
                if sides[side] + matchsticks[start] <= length:
                    sides[side] += matchsticks[start]
                    if dfs(start + 1):
                        return True
                    sides[side] -= matchsticks[start]

                if sides[side] == 0:
                    break
            return False

        return dfs(0)

        