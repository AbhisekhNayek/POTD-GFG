import heapq

class Solution:
    # Function to return the minimum cost to reach the bottom-right cell from the top-left cell.
    def minimumCostPath(self, grid):
        n = len(grid)
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))
        dis = [[float('inf')] * n for _ in range(n)]
        dis[0][0] = grid[0][0]
        
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]
        
        while pq:
            wt, i, j = heapq.heappop(pq)
            
            for k in range(4):
                x = i + dr[k]
                y = j + dc[k]
                
                if 0 <= x < n and 0 <= y < n and dis[x][y] > wt + grid[x][y]:
                    dis[x][y] = wt + grid[x][y]
                    heapq.heappush(pq, (dis[x][y], x, y))
        
        return dis[n-1][n-1]



#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends
