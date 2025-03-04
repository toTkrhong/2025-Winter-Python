import sys
input = sys.stdin.readline

N = int(input())
rank = []
for _ in range (N):
    rank.append(int(input()))
rank.sort()
bulman = 0
for i in range(N):
    bulman += abs(rank[i] - (i+1))
print(bulman)