class Solution:
    def twoRepeated(self, arr , n):
        result = []
        for i in range(n + 2):
            index = abs(arr[i])
            if arr[index] > 0:
                arr[index] = -arr[index]
            else:
                result.append(index)
        return result
