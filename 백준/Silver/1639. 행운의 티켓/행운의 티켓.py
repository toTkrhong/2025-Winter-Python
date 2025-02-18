import sys
input = sys.stdin.readline
output = sys.stdout.write

def golden_ticket(ticket):
    mid = len(ticket) // 2
    left = sum(ticket[:mid])
    right = sum(ticket[mid:])

    if (left == right):
        return True
    else:
        return False

ticket = list(map(int, input().strip()))

if len(ticket) % 2 == 0 :
    size = len(ticket)
else:
    size = len(ticket) - 1 

while size > 0:
    i = 0
    while i + size <= len(ticket):
        if golden_ticket(ticket[i:i + size]):
            print(size)
            exit()
        i += 1
    size -= 2 

print(0)