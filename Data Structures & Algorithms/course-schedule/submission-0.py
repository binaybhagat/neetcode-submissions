class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)        

        visited={}
        result = []
        def dfs(c):                
            if c in visited:
                return visited[c]
                
            visited[c] = True

            for i in graph[c]:
                if dfs(i):
                    return True
            
            visited[c]=False
            result.append(c)
            
        for c in graph:
            if dfs(c):
                result=[]
        
        return len(result) == numCourses
