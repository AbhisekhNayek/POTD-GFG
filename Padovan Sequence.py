#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        if n<3:
            return 1
        p1 = p2 = p3 = 1
        for i in range(n-2):
            p1, p2, p3 = p2, p3, (p1+p2)%(10**9+7)
        return p3

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends
