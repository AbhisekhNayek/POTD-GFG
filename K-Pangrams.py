#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        # code here
        string=string.split(" ")
        res=0
        for i in string:
            res+=len(i)
        if res<26:
            return False
        d={}
        for i in string:
            for j in i:
                d[j]=d.get(j,0)+1
        if len(d)==26:
            return True
        elif 26-len(d)<=k:
            return True
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends
