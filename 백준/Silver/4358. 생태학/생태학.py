import sys
input = sys.stdin.readline

trees = {}
name = " "
total = 0
while (True):
    name = input().strip()
    if name == '':
        break
    if name not in trees:
        trees[name] = 1
    else:
        trees[name] +=1
    total += 1

trees = sorted(trees.items())
for name, val in trees:
    print(f"{name} {(val/total)*100:.4f}")
