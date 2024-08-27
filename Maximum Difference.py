class Solution:
    def findMaxDiff(self, arr):
        ls=[0]*len(arr)
        rs=[0]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[i]<=stack[-1]:
                stack.pop()
            if not stack:
                ls[i]=0
            else:
                ls[i]=stack[-1]
            stack.append(arr[i])
        stack.clear()
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[i]<=stack[-1]:
                stack.pop()
            if not stack:
                rs[i]=0
            else:
                rs[i]=stack[-1]
            stack.append(arr[i])
        maxi=0
        for i in range(len(arr)):
            maxi=max(maxi,abs(ls[i]-rs[i]))
        return maxi


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends
