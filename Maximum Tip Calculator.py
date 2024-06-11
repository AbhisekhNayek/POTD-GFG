
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        a = [[0, 0] for _ in range(n)]
        for i in range(n):
            a[i][0] = arr[i]
            a[i][1] = brr[i]
        a.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

        ans = 0
        for i in a:
            if (i[0] > i[1] and x > 0) or (y == 0):
                ans += i[0]
                x -= 1
            else:
                ans += i[1]
                y -= 1
                
        return ans
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends
