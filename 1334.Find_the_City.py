class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Distance table: 0 to self, infinity elsewhere
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Add direct roads (both ways)
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        # Floyd-Warshall: This part finds the shortest distance between every pair of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        
        best_city = 0
        best_count = n

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:  # skip itself
                    count += 1

            if count <= best_count:
                best_city = i
                best_count = count

        return best_city
