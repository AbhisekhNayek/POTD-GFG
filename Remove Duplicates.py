class Solution:
    
    def remove_duplicates(self, input_str):
        result = ""
        for char in input_str:
            if char not in result:
                result += char
        return result
