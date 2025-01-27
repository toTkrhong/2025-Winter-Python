n, m = map(int, input().split())
original = []
cnt = []

for i in range(n):
    original.append(input())

for a in range(n-7):
    for b in range(m-7):
        white = 0
        black = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        white += 1
                    if original[i][j] != 'B':
                        black += 1
                else:
                    if original[i][j] != 'B':
                        white += 1
                    if original[i][j] != 'W':
                        black += 1
        cnt.append(min(white, black))

print(min(cnt))