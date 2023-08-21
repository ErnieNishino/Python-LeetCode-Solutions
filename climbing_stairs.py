# This solution is derived through mathematical reasoning.
# However, in practice, you can achieve a faster resolution using dynamic programming.
class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(n):
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

        def combination(n, m):
            if m > n:
                return 0
            return factorial(n) // (factorial(m) * factorial(n - m))

        if n % 2 == 0:
            res = 2
            for i in range(int(n/2 - 1)):
                res += combination(n-i-1, i+1)
        else:
            res = 1
            for j in range(int((n-1)/2)):
                res += combination(n-j-1, j+1)
        return res

# Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]