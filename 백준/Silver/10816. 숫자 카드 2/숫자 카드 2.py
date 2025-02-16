import sys
from collections import Counter

input = sys.stdin.read
output = sys.stdout.write

# 한 번에 모든 입력을 가져오기
data = input().split()

# 입력 데이터 분할
n = int(data[0])
given_card = map(int, data[1:n+1])  # 리스트 대신 map 사용
m = int(data[n+1])
finding_card = map(int, data[n+2:n+2+m])  # 리스트 대신 map 사용

# 카드 개수 세기
card_dict = Counter(given_card)  # Counter를 사용해 자동으로 개수 세기

# 결과 문자열을 한 번에 출력
output(" ".join(str(card_dict[item]) if item in card_dict else "0" for item in finding_card) + "\n")
