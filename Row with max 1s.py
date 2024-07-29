#User function Template for python3
class Solution:

	def rowWithMax1s(self, arr):
        max_count, max_index = 0, -1
        for i in range(len(arr)):
            if arr[i][-1] > max_count:
                max_count = arr[i][-1]
                max_index = i
            elif arr[i][-1] == max_count:
                max_index = i if sum(arr[i]) > sum(arr[max_index]) else max_index
        return max_index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
