input = input()
li = [char for char in input]

a_cnt = input.count('a')
circle = li + li[:a_cnt-1]

window = circle[:a_cnt].count('a')
max = window

for i in range(a_cnt, len(circle)):
    window += circle[i].count('a') - circle[i - a_cnt].count('a')
    if window > max:
        max = window

print(a_cnt-max)