import sys
input = sys.stdin.readline

N = int(input())

for _ in range (N):
    string = list(input().strip())
    left_cnt = 0; right_cnt = 0
    flag = True
    for i in range (len(string)):
        if (string[0] == ')') or (string[-1] == '('):
            flag = False
        else:
            if string[i] == '(':
                left_cnt+=1
            elif string[i] == ')':
                right_cnt+=1
                if right_cnt > left_cnt:
                    flag = False
    if left_cnt != right_cnt:
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")