num = int(input())

fact=1
for i in range(1, num+1):
    fact *= i

cnt=0
while (fact % 10 == 0):
    fact //= 10
    cnt+=1
print(cnt)