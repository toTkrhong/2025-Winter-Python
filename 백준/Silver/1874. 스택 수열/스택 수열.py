import sys

input = sys.stdin.readline

N = int(input().strip())
listt = [int(input().strip()) for _ in range(N)]

stack = []
result = []
n = 1

for i in listt:
    while n <= i:
        stack.append(n)
        result.append("+")
        n += 1
    
    if stack[-1] == i:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

print("\n".join(result))
