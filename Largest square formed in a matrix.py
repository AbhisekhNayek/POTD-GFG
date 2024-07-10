
from typing import List


class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # code here
        mxs=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:mxs=max(mxs,1)
                if i and j:
                    if mat[i-1][j-1] and mat[i-1][j] and mat[i][j-1] and mat[i][j]:
                        mat[i][j]=min(mat[i-1][j-1],mat[i-1][j],mat[i][j-1])+1
                        mxs=max(mxs,mat[i][j])
        return mxs
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        mat = IntMatrix().Input(n, m)

        obj = Solution()
        res = obj.maxSquare(n, m, mat)

        print(res)

# } Driver Code Ends
