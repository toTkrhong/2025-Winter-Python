import sys
input = sys.stdin.readline

n = int(input())
time = []
time = list(map(int, input().split()))
time.sort()

total = 0
tmp = 0
for i in range(0,n):
    sum = (tmp + time[i])
    tmp = sum
    total += sum
    
print(total)