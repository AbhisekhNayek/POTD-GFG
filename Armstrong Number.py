#User function Template for python3



class Solution:

  def armstrongNumber (self, n):

        return 'Yes' if sum([int(x)**3 for x in str(n)]) == n else 'No'


#{ 

 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        n = input()

        n=int(n)

        ob = Solution()

        print(ob.armstrongNumber(n))

# } Driver Code Ends
