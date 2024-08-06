#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        n = len(str)
        if(n>15 or n<7):
            return False
        line = str.split('.')
        k = len(line)
        if(k!=4):
            return False
        temp = 0
        for it in line:
            if((len(it)>1 and it[0]=='0') or len(it)==0):
                return False;
            temp = int(it)
            if(temp<0 or temp>255):
                return False
                
        return True;



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends
