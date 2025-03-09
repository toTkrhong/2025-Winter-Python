import sys
input = sys.stdin.readline

n = int(input())
ans = [float('inf')] * 1001 
ans[0] = 0; ans[1] = 1; ans[2] = 2
for i in range (3, n+1):
    ans[i] = (ans[i-1] + ans[i-2])%10007
print(ans[n])