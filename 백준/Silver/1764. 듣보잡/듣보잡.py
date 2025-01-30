l, s = map(int, input().split())
cnt=0
detbo = {}
detbo_list = []

for i in range(l):
   name = input()
   if name in detbo:
    detbo[name] += 1
   else:
    detbo[name] = 1

for i in range(s):
   name = input()
   if name in detbo:
    detbo[name] += 1
   else:
    detbo[name] = 1

for name in sorted(detbo.keys()):
   if detbo[name] > 1:
      cnt+=1
      detbo_list.append(name)

print(cnt)
for i in detbo_list:
   print(i)