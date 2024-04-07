class Solution:
    def maxDotProduct(self, n, m, a, b):
        # Initialize dp arrays with 0s
        dp_curr = [0] * (m + 1)
        dp_prev = [0] * (m + 1)

        for i in range(n):
            for j in range(min(m, i + 1)):
                dp_curr[j + 1] = max(dp_prev[j] + a[i] * b[j], dp_prev[j + 1])
            dp_prev = dp_curr[:]  # Update dp_prev with current row values
            dp_curr = [0] * (m + 1)  # Reset dp_curr for the next iteration

        return dp_prev[m]
