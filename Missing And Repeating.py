#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        dup = -1
        
        for i in range(n):
            if arr[abs(arr[i]) - 1] < 0:
                dup = abs(arr[i])
            else:
                arr[abs(arr[i]) - 1] *= -1
        
        total_sum = n * (n + 1) // 2
        arr_sum = sum(abs(x) for x in arr)
        missing = total_sum - (arr_sum - dup)
        
        return [dup, missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends
