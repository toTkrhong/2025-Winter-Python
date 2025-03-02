import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())

tuples = [tuple(map(int, input().split())) for _ in range (N)]

tuples.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(tuples[i][0], tuples[i][1])