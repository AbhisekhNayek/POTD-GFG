from collections import Counter

class Solution:
    def sameFreq(self, s):
        char_count = Counter(s)
        values_set = set(char_count.values())
        
        if len(values_set) == 1:
            return 1
        
        max_count = max(char_count.values())
        max_count_keys = [key for key, count in char_count.items() if count == max_count]
        
        for key in max_count_keys:
            char_count[key] -= 1
        
        return 1 if len(set(char_count.values())) == 1 else 0

# Example usage:
solution_instance = Solution()
result = solution_instance.sameFreq("aabbc")
print(result)
