#User function Template for python3

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        x = y = z = 0
    
        for i in range(n - 1):
            x = max(x, arr[i] + i)
            if i == y:
                y = x
                z += 1
    
        if y >= n - 1:
            return z
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends
