import sys
input = sys.stdin.readline

zero_cnt = [-1] * 41
one_cnt = [-1] * 41

def fibonacci(n):
    if n == 0:
        zero_cnt[n] = 1
        one_cnt[n] = 0
        return
    elif n == 1:
        zero_cnt[n] = 0
        one_cnt[n] = 1
        return
    
    if zero_cnt[n] != -1 and one_cnt[n] != -1:
        return
    
    fibonacci(n-1)
    fibonacci(n-2)
    
    zero_cnt[n] = zero_cnt[n-1] + zero_cnt[n-2]
    one_cnt[n] = one_cnt[n-1] + one_cnt[n-2]

case = int(input())

for _ in range(case):
    num = int(input())
    fibonacci(num)
    print(zero_cnt[num], one_cnt[num]) 
