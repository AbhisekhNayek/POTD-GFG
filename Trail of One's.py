#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        zero_invalid, one_invalid = 1, 1
        M = 10**9+7
        for _ in range(1, n):
            zero_invalid, one_invalid = (zero_invalid+one_invalid)%M, zero_invalid
        return (pow(2, n)%M + M - (zero_invalid+one_invalid))%M
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends
