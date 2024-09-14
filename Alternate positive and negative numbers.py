class Solution:
    def rearrange(self, arr):
        # Lists to store positive and negative numbers
        pos = []
        neg = []
        
        # Separate positive and negative numbers
        for num in arr:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        
        # Indexes for positive and negative lists
        i = 0
        j = 0
        k = 0
        
        # Merge the positive and negative numbers alternately
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            arr[k] = neg[j]
            k += 1
            i += 1
            j += 1
        
        # If there are remaining positive numbers
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1
        
        # If there are remaining negative numbers
        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1
