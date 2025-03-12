import sys
from collections import Counter

input = sys.stdin.readline

# 입력
n, m, b = map(int, input().split())
ground = []
block_count = Counter()

# 블록 개수를 Counter로 저장
for _ in range(n):
    row = list(map(int, input().split()))
    for height in row:
        block_count[height] += 1  # 각 높이별 개수 저장

# 높이 범위 설정
low = min(block_count)
high = max(block_count)

ans_time = float('inf')
ans_height = 0

# 가능한 모든 높이 탐색
for level in range(low, high+1):
    remove = 0
    fill = 0

    # 각 높이에 대해 연산 수행 (O(256)으로 해결 가능)
    for height, count in block_count.items():
        if height > level:
            remove += (height - level) * count  # 블록 제거
        elif height < level:
            fill += (level - height) * count  # 블록 채우기
    
    # 블록을 채울 수 있는 경우만 진행
    if remove + b >= fill:
        time = (remove * 2) + fill
        if time < ans_time or (time == ans_time and level > ans_height):
            ans_time = time
            ans_height = level

# 출력
print(ans_time, ans_height)
