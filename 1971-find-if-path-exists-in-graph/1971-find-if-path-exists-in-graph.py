class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True

        adj = [[] for _ in range(n)]

        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = {source}
        q = deque([source])

        while q :
            
            node = q.popleft()
            for nei in adj[node]:
                if nei == destination: return True
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return False