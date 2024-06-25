class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        m=len(mat)
        for i in range(m):
            n=len(mat[i])
            arr = mat[i][k%n:n]+mat[i][:k%n]
            mat[i]=arr
        
        return mat



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends
