class Solution:
    def minSteps(self, d):
        jump, position = 0,0
        while position < d or (position - d)%2 != 0:
            jump += 1
            position += jump
        return jump
