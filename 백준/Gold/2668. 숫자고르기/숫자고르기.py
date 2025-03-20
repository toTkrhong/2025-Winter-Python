import sys
input = sys.stdin.readline

def dfs(start, current, num_list, visited, selected):
    if visited[current]:
        return current == start 

    visited[current] = True 
    next_num = num_list[current]

    cycle_found = dfs(start, next_num, num_list, visited, selected)

    if cycle_found:
        selected.add(current)

    return cycle_found

n = int(input().strip())

num_list = [-1] * (n + 1)
selected = set()

for i in range(1, n + 1):
    num_list[i] = int(input().strip())

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i, num_list, visited, selected)

print(len(selected))
for num in sorted(selected):
    print(num)
