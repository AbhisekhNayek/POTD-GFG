class Solution:
    def search(self, pattern, text):
        occurrences = []
        for i in range(len(text) - len(pattern) + 1):
            if text[i:].startswith(pattern):
                occurrences.append(i + 1)
        return occurrences
