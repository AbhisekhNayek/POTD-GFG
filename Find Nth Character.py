class Solution:
    def nthCharacter(self, s, r, n):
        def calculate_length(r):
            return 2**(r-1)

        def get_next_sequence(a, b):
            return a + b, b + a

        current_length = calculate_length(r)
        current_sequence = ("0", "1") if s == "0" else ("1", "0")

        while n >= current_length:
            current_length *= 2
            current_sequence = get_next_sequence(*current_sequence)

        return current_sequence[n]

# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
