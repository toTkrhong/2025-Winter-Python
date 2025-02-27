import sys
input = sys.stdin.readline

N = int(input())
ex = {}

for _ in range (N):
    file = input().split('.')[1].strip()
    if file not in ex:
        ex[file] = 1
    else:
        ex[file]+=1

ex = dict(sorted(ex.items()))

for items in ex:
    print(items, ex[items])