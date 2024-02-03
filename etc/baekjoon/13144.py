# 1. 틀린 풀이 (중복 조합, Counter...)

# 길이 N - 수열
# 연속으로 n번(>=1) 숫자 뽑음 -> 같은 수가 아닐 확률

from sys import stdin
from itertools import combinations_with_replacement
from collections import Counter

N = int(stdin.readline().rstrip())  # 수열 길이
nums = [*map(int, stdin.readline().split())]  # 수열

# n번 뽑기 -> 중복 조합?
# 1..n번 -> 중복 조합 -> 같은 수 없을 때만 체크
# 연속으로 1번이라도 나오면 안됨 - 직접 구현 / counter

res = []
for i in range(1, len(nums)):
    if i < 2:
        continue
    
    coms = list(combinations_with_replacement(nums, i))
    for com in coms:
        if Counter(com).most_common(1)[0][1] == 1:
            res.append(com)

cnt = len(res)

if Counter(nums).most_common(1)[0][1] == len(nums):
    cnt += len(nums)

# print(cnt)
print(res)
        



# 2. 그리디 문제 -> 투포인터 풀이
# 길이 N - 수열
# 연속으로 n번(>=1) 숫자 뽑음 -> 같은 수가 아닐 확률

from sys import stdin
from itertools import combinations_with_replacement
from collections import Counter

N = int(stdin.readline().rstrip())  # 수열 길이
nums = [*map(int, stdin.readline().split())]  # 수열

# n번 뽑기 -> 중복 조합? => X -> 그리디: 투포인터..
temp = [0] * 100001
start, end = 0, 0
res = 0
while end < N:
    if not temp[nums[end]]:
        temp[nums[end]] +=1
        end +=1
    else:
        res += (end - start)
        temp[nums[start]] -= 1
        start += 1

res += ((end - start) * (end - start + 1)) // 2
print(res)