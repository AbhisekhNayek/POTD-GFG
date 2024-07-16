#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		pos = 0

	    for c in s:
	        count, pos = count - int( c == ch ), pos+1
	        if not count : return s[pos:]

	    return ""


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends
