class Solution:
    def celebrity(self, mat):
        n = len(mat)
        for i, k in enumerate(mat):
            if sum(k) == 0 and sum([mat[j][i] for j in range(n)]) == n-1:
                return i
        return -1


#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends
