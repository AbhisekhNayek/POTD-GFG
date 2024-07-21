#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        mod = 10**9 + 7
        maxmul = 1
        maxnum = float('-inf')
        count_neg = 0
        count_zero = 0

        for num in arr:
            if num == 0:
                count_zero += 1
                continue
            if num < 0:
                count_neg += 1
                maxnum = max(maxnum, num)
            maxmul = (maxmul * num) % mod

        # If all elements are zero
        if count_zero == len(arr):
            return 0

        # If there is an odd number of negative numbers, exclude the largest negative number
        if count_neg % 2 != 0:
            maxmul = (maxmul * pow(maxnum, mod-2, mod)) % mod

        return maxmul

    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends
