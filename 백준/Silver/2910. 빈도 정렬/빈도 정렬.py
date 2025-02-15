import sys
input = sys.stdin.readline
output = sys.stdout.write

n, c = map(int, input().split())
code = []
code_dict = {}
code.extend(map(int, input().split()))
order = 1

#code_dict[item][0] = cnt
#code_dict[item][1] = order
for item in code:
    if item in code_dict:
        code_dict[item][0] += 1
    else:
        code_dict[item] = [1, order]
        order += 1

sorted_list = sorted(code_dict.items(), key=lambda x: (-x[1][0], x[1][1]))
for i in range (len(sorted_list)):
    output((str(sorted_list[i][0])+ " ") * sorted_list[i][1][0])