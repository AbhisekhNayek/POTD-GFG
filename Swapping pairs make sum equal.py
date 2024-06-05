class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        temp1 = sum(a)
        temp2 = sum(b)
        
        if temp1 == temp2:
            return 1;
        
        a.sort()
        b.sort()
        
        i ,j = 0 , 0
        
        while i < n and j < m:
            sumOf_a = temp1 - a[i] + b[j]
            sumOf_b = temp2 - b[j] + a[i]
            
            if sumOf_a == sumOf_b:
                return 1;
            elif sumOf_a > sumOf_b:
                i += 1
            else:
                j += 1
        
        return -1
