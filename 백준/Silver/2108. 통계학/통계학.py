import sys
input = sys.stdin.readline

N = int(input())
numbers = []
total = 0

for _ in range (N):
    num = int(input())
    numbers.append(num)
    total += num

print(round(total/N)) #산술 평균

numbers.sort()
print(numbers[N//2]) #중앙값

num_cnt={}
max_cnt = 0
for items in numbers:
    if items in num_cnt:
        num_cnt[items] += 1
    else:
        num_cnt[items] = 1
    if num_cnt[items] > max_cnt:
        max_cnt = num_cnt[items]

mod = []
for items in num_cnt:
    if num_cnt[items] == max_cnt:
        mod.append(items)

mod.sort()
if len(mod) == 1:
    print(mod[0])
else:
    print(mod[1])

rang = numbers[-1] - numbers[0]
print(rang) #범위
