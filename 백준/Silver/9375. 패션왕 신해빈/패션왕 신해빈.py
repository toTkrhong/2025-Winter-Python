import sys
input = sys.stdin.readline

n = int(input())

for _ in range (n):
    ea = int(input())
    dict = {}

    for i in range (ea):
        cloth, category = input().split()

        if category in dict: #카테고리가 사전에 있으면 카테고리에 의상을 추가
            dict[category].append(cloth)
        else:
            dict[category] = [cloth] #사전에 카테고리가 없으면 새로 생성하고 카테고리에 옷넣기
    ans = 1
    for keys in dict:
        ans *= (len(dict[keys])+1)
        

    print(ans-1)
