import sys
input = sys.stdin.readline

N = int(input())
a = set(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

for item in b:
    print(1 if item in a else 0)