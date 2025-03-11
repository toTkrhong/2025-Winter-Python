import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
books = []
for _ in range (n):
    books.append(input().strip())
books.sort()

print(Counter(books).most_common(1)[0][0])