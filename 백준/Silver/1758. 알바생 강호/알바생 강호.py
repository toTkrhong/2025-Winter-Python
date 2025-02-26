import sys
input = sys.stdin.readline

N = int(input())
customers = []

for _ in range (N):
    customers.append(int(input()))

customers.sort(reverse=True)
tip = 0
for i in range (N):
    if (customers[i] - i) >= 0:
        tip += (customers[i] - i)
    else:
        continue
print(tip)