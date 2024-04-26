class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
        outside = lambda r, c: r < 0 or c < 0 or r >= n or c >= m
        cur, dir = 0+0j, 1+0j
        while True:
            r, c = int(cur.imag), int(cur.real)
            if matrix[r][c] == 1:
                matrix[r][c] = 0
                dir *= 1j
            else:
                ncur = cur+dir
                nr, nc = int(ncur.imag), int(ncur.real)
                if outside(nr, nc):
                    return int(cur.imag), int(cur.real)
                cur = ncur
        return 0, 0
