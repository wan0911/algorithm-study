# 숫자, 알파벳 소문자
# 숫자 앞에 0은 제거
## words에 존재하는 숫자를 모두 찾는다 -> result에 append -> 비내림차순(오름차순) 정렬
## 같은 숫자가 여러개면 -> 모두 출력

# 1. 정규식: a-z 인덱스 찾기 -> slicing
# 2. 반복문

from sys import stdin
import re

N = int(stdin.readline().rstrip())
words = [stdin.readline().rstrip() for _ in range(N)]

# 정규식
nums = []
for word in words:
    nums.extend(re.findall("[^a-z]+", word))


res = []
for num in nums:
    if int(num) == 0 or sum([int(n) for n in nums]) == 0:
        res.append(0)
        continue

    # 문자 앞 0 제거
    res.append(int(num.lstrip("0")))

for n in sorted(res):
    print(n)
