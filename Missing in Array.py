class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        r=n*(n+1)//2
        return abs(sum(arr)-r)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends
