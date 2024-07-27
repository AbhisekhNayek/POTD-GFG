#User function Template for python3

class Solution:
    def solve(self,i,j,s):
        if i>=j:
            return 0
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        if s[i]==s[j]:
            self.dp[i][j]= self.solve(i+1,j-1,s)
            return self.dp[i][j]
        else:
            self.dp[i][j] = min(1+self.solve(i+1,j,s),1+self.solve(i,j-1,s))
            return self.dp[i][j]
    def countMin(self, str):
        
        j = len(str)
        self.dp =[[-1]*j for _ in range(j)]
        j = j-1
        return self.solve(0,j,str)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends
