import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
ans = -1
while (n >= 2):
    if n%5==0:
        cnt+=n/5
        n=0
    else:
        cnt+=1
        n-=2

if n == 0:
    print(int(cnt))
else:
    print("-1")
