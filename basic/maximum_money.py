class Solution:
    def maximizeMoney(self, N, K):
        # code here
        if N % 2 == 0:
            return (K * int(N/2))
        else:
            return (K * (int(N/2) + 1))
