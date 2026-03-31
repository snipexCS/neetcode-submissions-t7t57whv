class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMax = {i:[] for i in range(numCourses)}
        for crs , pre in prerequisites:
            preMax[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMax[crs] == []:
                return True
            

            visiting.add(crs)
            for pre in preMax[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMax[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        