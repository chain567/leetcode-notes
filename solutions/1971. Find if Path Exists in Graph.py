class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj_mat = defaultdict(list)
        for i, j in edges:
            adj_mat[i].append(j)
            adj_mat[j].append(i)
        q = deque([source])
        seen = set()
        while q:
            node = q.popleft()
            if node == destination:
                return True
            seen.add(node)
            for z in adj_mat[node]:
                if z not in seen:
                    q.append(z)
        return False