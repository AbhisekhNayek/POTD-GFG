#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
       
        dp = [[0]*(W+1) for _ in range(len(val)+1)]
        for i in range(len(wt)):
            for w in range(1, W+1):
                dp[i+1][w] = dp[i][w]
                if wt[i] <= w:
                    dp[i+1][w] = max(dp[i+1][w], dp[i][w-wt[i]]+val[i])
        return dp[-1][W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends
