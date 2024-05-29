class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        dp = [True] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = (
                    i - x == 0 or
                    i - y == 0 or
                    (i - 1 > 0 and not dp[i - 1]) or
                    (i - x > 0 and not dp[i - x]) or
                    (i - y > 0 and not dp[i - y])
                )
        return int(dp[n])
