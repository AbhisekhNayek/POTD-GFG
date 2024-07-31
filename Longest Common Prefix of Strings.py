#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        if len(arr)==1:
            return arr[0]
        ans=[]
        M = min(arr,key=len)
        m=len(M)
        n=len(arr)
        for i in range(n-1):
            c=''
            for j in range(m):
                if arr[i][j]==arr[i+1][j]:
                    c+=arr[i][j]
                else:
                    # return -1
                    break
            if c!='':
                ans.append(c)
        
        if len(ans)>=n-1:
            a=min(ans,key=len)
            return a
        
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends
