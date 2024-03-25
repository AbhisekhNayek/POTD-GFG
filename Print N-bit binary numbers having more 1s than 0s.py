class Solution:
    
    def generate_NBit_binary(self, n):
        result = []
        self.generate_helper("", 0, 0, n, result)
        return result
    
    def generate_helper(self, binary, count_0, len_of_binary, n, result):
        # Base case: if the length of the binary string reaches n, append it to the result
        if len_of_binary == n:
            result.append(binary)
            return
        
        # Append '1' and recursively call with incremented length
        self.generate_helper(binary + "1", count_0, len_of_binary + 1, n, result)
        
        # If the count of 0s is less than half the total length, append '0' and recursively call with incremented length and count of 0s
        if count_0 * 2 < len_of_binary:
            self.generate_helper(binary + "0", count_0 + 1, len_of_binary + 1, n, result)

# Example usage:
sol = Solution()
n = 3
print(sol.generate_NBit_binary(n))
