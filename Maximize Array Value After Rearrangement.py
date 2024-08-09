#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        # arr = [5, 3, 2, 4, 1]
        arr.sort()
        sum1 = 0
        mod = 10**9+7
        for i in range(0, len(arr)):
            sum1 = sum1 + i * arr[i]
        return sum1 % mod
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends
