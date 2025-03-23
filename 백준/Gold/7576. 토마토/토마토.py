import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

box = []
for _ in range (m):
    box.append(list(map(int, input().split())))

day = 0
queue = deque()
updown = [0, 0, -1, 1]
leftright = [-1, 1, 0, 0]

for i in range (m):
    for j in range (n):
        if box[i][j] == 1:
            queue.append((i, j))

while (queue):
    tmp = []
    while (queue):
        x, y = queue.popleft()
        for i in range (4):
            xx, yy = x + leftright[i], y + updown[i]
            if 0 <= xx < m and 0 <= yy < n and box[xx][yy] == 0:
                box[xx][yy] += 1
                tmp.append((xx, yy))
    '''print()
    for i in range (m):
            print()
            for j in range (n):
                print(box[i][j], end='')'''
    for items in tmp:
        queue.append(items)
    day+=1

for tomato in box:
    if 0 in tomato:
        print(-1)
        break
else:
    print(day-1)