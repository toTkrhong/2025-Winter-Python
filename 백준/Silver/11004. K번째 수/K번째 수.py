import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = []
num.extend(map(int, input().split()))
num.sort()
print(num[m-1])