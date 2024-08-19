#User function Template for python3


class Solution:
    def partition(arr, low, high):
        # take the last element as pivot
        pivot = arr[high]
        # pointer to the larger element than pivot
        i = low - 1
    
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1 # increase the pointer by 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
        temp = arr[i+1]
        arr[i+1] = arr[high]
        arr[high] = temp
    
        return i+1
    
    def quickSelect(arr, low, high, k):
        pi = Solution.partition(arr, low, high)
    
        if pi == k:
            return arr[pi]
        elif pi > k:
            return Solution.quickSelect(arr, low, pi-1, k)
        else:
            return Solution.quickSelect(arr, pi+1, high, k)

    def kthSmallest(self, arr,k):
        # arr.sort()
        # return arr[k-1]
        return  Solution.quickSelect(arr, 0, len(arr)-1, k-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends
