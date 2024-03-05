def maxIndexDiff(a, n):
    left_min = [float('inf')] * n
    right_max = [float('-inf')] * n

    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(a[i], left_min[i-1])

    right_max[n-1] = a[n-1]
    for j in range(n-2, -1, -1):
        right_max[j] = max(a[j], right_max[j+1])

    i, j = 0, 0
    max_diff = -1

    while i < n and j < n:
        if right_max[j] >= left_min[i]:
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1

    return max_diff
