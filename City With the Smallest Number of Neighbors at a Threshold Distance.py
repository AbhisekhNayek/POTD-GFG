class Solution:
    def findCity(self, n: int, m: int, edges: list, distanceThreshold: int) -> int:
        # Initialize adjacency matrix with infinite distance
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]

        # Populate adjacency matrix with given edge weights
        for src, dest, cost in edges:
            dist[src][dest] = cost
            dist[dest][src] = cost

        # Floyd-Warshall algorithm for all pairs shortest path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        min_city = -1
        min_neighbors = n

        # Count reachable cities for each city
        for i in range(n):
            reachable_cities = sum(1 for d in dist[i] if d <= distanceThreshold)
            reachable_cities -= 1  # Exclude self
            if reachable_cities < min_neighbors or (reachable_cities == min_neighbors and i > min_city):
                min_neighbors = reachable_cities
                min_city = i

        return min_city
