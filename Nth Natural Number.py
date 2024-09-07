#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        ans=""
        while n:
            ans=str(n%9)+ans
            n//=9
        return int(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends
