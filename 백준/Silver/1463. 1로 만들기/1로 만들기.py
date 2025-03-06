import sys
input = sys.stdin.readline

n = int(input())
m=n
dp = [float('inf')]*(n+1)
dp[1] = 0
for n in range(2, n+1):
    dp[n] = dp[n-1]+1
    if n%3==0:
        dp[n] = min(dp[n], dp[n//3]+1)
    if n%2==0:
        dp[n] = min(dp[n], dp[n//2]+1)
print(int(dp[n]))