from operator import xor
from functools import reduce


class Solution:
    def findSingle(self, n, arr):
        return reduce(xor, arr)
