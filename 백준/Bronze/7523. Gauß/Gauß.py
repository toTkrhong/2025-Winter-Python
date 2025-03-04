import sys
input = sys.stdin.readline

N = int(input())
for j in range (N):
    a, b = map(int, input().split())
    sum = (a+b)*(b-a+1)//2
    print(f'Scenario #{j+1}:')
    print(int(sum),"\n")