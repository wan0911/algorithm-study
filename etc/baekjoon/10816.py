# 1.
# 숫자 카드 N개, 정수 M
# M이 적혀있는 카드를 N개 중에 몇 개를 가지고 있을지?

from sys import stdin
from collections import Counter

N = int(stdin.readline().rstrip())
cards = [*map(int, stdin.readline().split())]
M = int(stdin.readline().rstrip())
nums = [*map(int, stdin.readline().split())]

cards_count = Counter(cards)
res = []
for num in nums:
    if num in cards_count:
        res.append(cards_count[num])
    else:
        res.append(0)
    
print(*res)
    
    
# 2. Counter를 안쓰고 풀려면... 
## 1. not in 체크
## 2. 완탐하면서 pop을 해야하나? 


'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''