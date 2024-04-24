class Solution:
    def ways(self, x, y):
        mod = 1000000007
        
        # Initialize dp array with zeros
        dp = [0] * (min(x, y) + 1)

        # Base case: There is only one path to reach the origin (0, 0)
        dp[0] = 1

        # Calculate the number of paths for each point along the diagonal
        for i in range(1, min(x, y) + 1):
            dp[i] = (dp[i - 1] * (x + y - i + 1) * pow(i, mod - 2, mod)) % mod

        return dp[min(x, y)]
