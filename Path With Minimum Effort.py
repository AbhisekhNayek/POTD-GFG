from typing import List

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        def dfs(mid):
            stack = [(0, 0)]
            visited = set()
            while stack:
                x, y = stack.pop()
                if x == rows - 1 and y == columns - 1:
                    return True
                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < columns and (nx, ny) not in visited and abs(heights[nx][ny] - heights[x][y]) <= mid:
                        stack.append((nx, ny))
            return False
        
        left, right, result = 0, int(1e6), float('inf')
        while left <= right:
            mid = (left + right) // 2
            if dfs(mid):
                result, right = mid, mid - 1
            else:
                left = mid + 1
        return result
