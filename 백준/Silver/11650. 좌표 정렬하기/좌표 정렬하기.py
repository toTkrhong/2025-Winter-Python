num = int(input())

xy = [["" for row in range(2)]for col in range(num)]

for i in range (num):
    xy[i][0], xy[i][1] = input().split()
    xy[i][0] = int(xy[i][0]); xy[i][1] = int(xy[i][1])

xy.sort()
for i in range (num):
    print(xy[i][0], xy[i][1])