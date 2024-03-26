class Solution:
    def isAdditiveSequence(self, num_str: str) -> bool:
        if len(num_str) < 3:
            return False
        
        def is_valid_number(s):
            return len(s) == 1 or s[0] != '0'
        
        for i in range(1, len(num_str) - 1):
            if not is_valid_number(num_str[:i]):
                continue
            for j in range(i + 1, len(num_str)):
                if not is_valid_number(num_str[i:j]):
                    continue
                num1 = int(num_str[:i])
                num2 = int(num_str[i:j])
                k = j
                while k < len(num_str):
                    num3 = num1 + num2
                    num3_str = str(num3)
                    if not num_str.startswith(num3_str, k):
                        break
                    k += len(num3_str)
                    num1, num2 = num2, num3
                    if k == len(num_str):
                        return True
        return False
