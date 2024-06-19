# 숫자+문자열 -> 숫자만 추출해서 자연수 만들기 -> 그 자연수의 약수
# 자연수 <= 100,000,000 / 앞자리 00은 고려 X
# 완탐 가능?

import sys

input = sys.stdin.readline

# 문자열 -> 숫자
word = "".join([s for s in input() if s.isdigit()]).lstrip("0") 
# lstrip 없이, 바로 Int 써도 되긴 함
num = int(word) 

# 약수 구하기 -> 완탐 (이진으로 풀면 안됨..)
cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(cnt)


"""
g0en2Ts8eSoft
"""
