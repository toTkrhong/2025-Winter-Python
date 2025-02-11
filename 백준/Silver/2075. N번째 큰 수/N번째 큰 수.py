import sys
import heapq
input = sys.stdin.readline
num = int(input())

num_heap = []
for i in range (num):
    tmp_list = map(int, input().split())
    for item in tmp_list:
      if len(num_heap) < num:
         heapq.heappush(num_heap, item)
      else:
         heapq.heappushpop(num_heap, item)
print(num_heap[0])