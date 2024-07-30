from typing import List

class Solution:
    def findPath(self, mat):
        m=len(mat)
        ret=set()
        def dfs(x=0,y=0,path=''):
            nonlocal mat,m,ret
            if not (0<=x<m and 0<=y<m):
                return
            if mat[y][x]==0:
                return
            if x==m-1 and y==m-1:
                ret.add(path)
                return
            mat[y][x]=0
            dfs(x+1,y,path+'R')
            dfs(x-1,y,path+'L')
            dfs(x,y+1,path+'D')
            dfs(x,y-1,path+'U')
            mat[y][x]=1
        dfs()
        return sorted(ret)


#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends
