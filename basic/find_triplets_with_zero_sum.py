#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.
    def findTriplets(self, arr, n):
        if n < 3:
            return 0

        if all(i > 0 for i in arr):
            return 0

        if all(i < 0 for i in arr):
            return 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        return 1

        return 0
# } Driver Code Ends
