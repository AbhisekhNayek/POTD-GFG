class Solution:
	def findMinCost(self, x, y, costX, costY):
		# code here
        dp = [[0]*(len(y)+1) for _ in range(len(x)+1)]
        for i in range(1, len(x)+1):
            dp[i][0] = i*costX
        for j in range(1, len(y)+1):
            dp[0][j] = j*costY
            
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j] + costY, dp[i][j+1] + costX)
        return dp[-1][-1]
