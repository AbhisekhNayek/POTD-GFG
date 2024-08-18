class Solution:
    def canSplit(self, arr):
        #code here
        total_sum = sum(arr)

        leftsum = 0

        for ind, elem in enumerate(arr):
            total_sum -= elem
            leftsum += elem
            if total_sum == leftsum:
                return True

        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends
