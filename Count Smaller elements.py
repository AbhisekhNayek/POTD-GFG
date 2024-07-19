#User function Template for python3

from sortedcontainers import SortedList

class Solution:
    def constructLowerArray(self, arr):
        # Initialize a SortedList to maintain elements in sorted order
        l = SortedList()
        
        # Initialize the output list with zeros, same length as the input array
        output = [0] * len(arr)
        
        # Iterate over the input array in reverse order
        for i in reversed(range(len(arr))):
            # Add the current element to the SortedList
            l.add(arr[i])
            
            # Find the index of the current element in the SortedList
            # This index represents the count of smaller elements to the right
            output[i] = l.index(arr[i])
        
        # Return the constructed output array
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
