class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Distance table: 0 to self, infinity elsewhere
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Add direct roads (both ways)
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        # Floyd-Warshall: try every city k as a middle stop
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


        best_city, best_count = 0, n
        for i in range(n):
            count = sum(d <= distanceThreshold for d in dist[i]) - 1  # -1 skips itself
            if count <= best_count:
                best_city, best_count = i, count


        return best_city
