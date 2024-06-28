#User function Template for python3

class Solution:
    def pattern (self, arr):
    # code here
        n = len(arr)
    
    # Check rows for palindromes
        for i in range(n):
            if arr[i] == arr[i][::-1]:
                return "{} R".format(i)
    
    # Check columns for palindromes
        for i in range(n):
            column = [arr[j][i] for j in range(n)]
            if column == column[::-1]:
                return "{} C".format(i)
    
    # No palindrome found
        return "-1"



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends
