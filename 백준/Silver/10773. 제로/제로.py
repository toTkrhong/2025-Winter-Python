k = int(input())
money = []

for i in range(k):
   num = int(input())
   if num == 0:
      money.pop()
   else:
      money.append(num)
print(sum(money))