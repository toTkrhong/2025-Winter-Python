import sys
input = sys.stdin.readline
from collections import deque
que = deque()
n = int(input())

for _ in range (n):
    command = input().split()
    if command[0] == 'push':
        que.append(int(command[1]))
    
    elif command[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    
    elif command[0] == 'size':
        print(len(que))
    
    elif command[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])

    elif command[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

    else:
        exit()