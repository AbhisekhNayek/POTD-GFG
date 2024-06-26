#User function Template for python3

class Solution:
    def number_coverage(self,i,j,matrix):
        n=len(matrix)
        m=len(matrix[0])
        res=0
        if (0<=i-1 and i-1<n) and (0<=j and j<m)     :
            if matrix[i-1][j]==1 and matrix[i][j]==0:
                res+=1
              
        if (0<=i+1 and i+1<n) and (0<=j and j<m)     :
            if matrix[i+1][j]==1 and matrix[i][j]==0:
                res+=1
        if (0<=j-1 and j-1<m) and (0<=i and i<n)     :
            if matrix[i][j-1]==1 and matrix[i][j]==0:
                res+=1
              
        if (0<=j+1 and j+1<m) and (0<=i and i<n)     :
            if matrix[i][j+1]==1 and matrix[i][j]==0:
                res+=1
        return res
    def findCoverage(self, matrix):
        sol=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sol+=self.number_coverage(i,j,matrix)
        return sol


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends
