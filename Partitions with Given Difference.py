from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        s = sum(arr)
        if (s-d)&1 != 0 or s < d:
            return 0

        s = (s-d)//2
 
        dp = [[0]*(n+1) for _ in range(s+1)]
        dp[0][0] = 1
            
        for s0 in range(0, s+1):
            for i in range(1, n+1):
                dp[s0][i] = dp[s0][i-1]
                if s0-arr[i-1] >= 0:
                    dp[s0][i] = (dp[s0][i]+dp[s0-arr[i-1]][i-1])%(10**9+7)

        return dp[s][n]
