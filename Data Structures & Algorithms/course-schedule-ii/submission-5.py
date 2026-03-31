class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMax = {c:[] for c in range(numCourses)}
        for pre , crs in prerequisites:
            preMax[pre].append(crs)

        res = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preMax[crs]:
                if  dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True



        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
        