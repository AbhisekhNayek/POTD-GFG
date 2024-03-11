from bisect import bisect_left

def countPairs(self, mat1, mat2, n, x):
    ans = 0

    for row in mat1:
        for y in row:
            target = x - y
            row_idx = bisect_left(mat2, [target])

            if row_idx > 0:
                col_idx = bisect_left(mat2[row_idx - 1], target)
                if col_idx < n and mat2[row_idx - 1][col_idx] == target:
                    ans += 1

    return ans
