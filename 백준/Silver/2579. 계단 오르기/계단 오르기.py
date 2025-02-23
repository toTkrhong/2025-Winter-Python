import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]

for _ in range(n):
    stairs.append(int(input()))

score = [0] * (n+1)
score[1] = stairs[1]
if (n==1):
    print(score[n])
    exit()
score[2] = stairs[1] + stairs[2]
if (n==2):
    print(score[n])
    exit()
score[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
if (n==3):
    print(score[n])
    exit()

for i in range(4, n+1):
    a = score[i-2] + stairs[i]
    b = score[i-3] + stairs[i-1] + stairs[i]
    score[i] = (max(a, b))
print(score[n])