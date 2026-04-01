class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        adj = [[] for _ in range(n)]
        for v,u in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        visited = set()
        def dfs(val,ngh):
            if val in visited:
                return False
            visited.add(val)
            for neigh in adj[val]:
                if neigh == ngh:
                    continue
                if not dfs(neigh,val):
                    return False
            return True

        


        return dfs(0,-1) and len(visited) == n