import sys
import math
input = sys.stdin.readline
# 입력 받기
b, c, a1, a2 = map(int, input().split())

# 특성방정식의 근 구하기
discriminant = math.sqrt(b**2 + 4*c)
r1 = (b + discriminant) / 2
r2 = (b - discriminant) / 2

# 절댓값이 더 큰 근 선택
result = max(r1, r2)

# 소수점 9자리까지 출력
print(f"{result:.9f}")
