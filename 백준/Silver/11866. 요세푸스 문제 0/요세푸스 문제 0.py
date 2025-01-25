N, k = map(int, input().split())

circle=[i+1 for i in range(N)]
eli=0
pop=0
poplist = []
while circle:
    eli+= (k-1)
    while eli >= len(circle):
        eli = eli - len(circle)
    pop = circle.pop(eli)
    poplist.append(pop)
output = "<" + ", ".join(map(str, poplist)) + ">"
print(output)
