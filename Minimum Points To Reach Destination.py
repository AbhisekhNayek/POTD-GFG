class Solution:
    def minPoints(self, rows, cols, points):
        dp = [[0] * cols for _ in range(rows)]
        
        # Fill the dp table from bottom-right to top-left
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    dp[i][j] = max(1, 1 - points[i][j])
                elif i == rows - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - points[i][j])
                elif j == cols - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - points[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - points[i][j])
        
        return dp[0][0]
