import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
given_card = list(map(int, input().split()))

card_dict = {}

m = int(input())
finding_card = list(map(int, input().split()))

for item in given_card:
    if item not in card_dict:
        card_dict[item] = 1
    else:
        card_dict[item] += 1

for item in finding_card:
    if item in card_dict:
        output(str(card_dict[item]) + " ")
    else:
        output("0 ")