class Solution:
    
    def findMissing(self, a, b, n, m):
        # Convert array b to a set for efficient lookup
        set_b = set(b)
        
        # Initialize a list to store missing elements
        missing_elements = []
        
        # Iterate over elements of array a
        for num in a:
            
        # If num is not present in set_b, it's a missing element
            if num not in set_b:
                missing_elements.append(num)
        
        return missing_elements
