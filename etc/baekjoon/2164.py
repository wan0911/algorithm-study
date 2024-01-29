# 1. 규칙 찾기.. -> 
# 1(위)~N(아래) 카드
# 1장 남을 때까지 / 제일 위 -> 버림, 아래로
# 마지막에 남는 1장 숫자

# 홀수 제거
from sys import stdin

N = int(stdin.readline().rstrip())
cards = [i for i in range(1, N+1)]
even_cards = cards[1::2]
print(temp)

if N%2 == 0:
    print(even_cards[-1])
else:
    
    
    
# 2. deque 라이브러리를 쓰면 시간 내에?
# 1(위)~N(아래) 카드
# 1장 남을 때까지 / 제일 위 -> 버림, 아래로
# 마지막에 남는 1장 숫자

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
cards = deque([i for i in range(1, N+1)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)