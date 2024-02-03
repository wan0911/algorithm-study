# 소수 = 에라토스테네스의 체? / 신기한 소수 비슷
# 연속된 소수의 합 (모두)
# 중복되면 안됨, 한 세트라도 있으면 ok
# N때문에 완탐 x?

# 1. 통과
# 소수 = 에라토스테네스의 체? / 신기한 소수 비슷
# 연속된 소수의 합 (모두)
# 중복되면 안됨, 한 세트라도 있으면 ok
# N때문에 완탐 x?

from sys import stdin

N = int(stdin.readline().rstrip())

# 자리수에 해당하는 신기한 소수 구하기
# 1. 소수가 아닌 수들의 배수 제거
## 예를 들어, 14 -> 14제곱근 = 3.xx = 4
# 2. 소수만 취합

# N이 주어지면, N 이하의 소수를 모두 구하고, 그 소수들의 합으로 N을 구할 수 있나? -> 이건 완탐일듯?, "연속된"
nums = [False,False] + [True]*(N-1)
for i in range(2, int(N**0.5)+1):
    if nums[i]:
        nums[i*2::i] = [False]*((N-i)//i)

primes = []
for i in range(N+1):
    if nums[i] == True:
        primes.append(i)

# 전부 연속되어야 함 -> 0번째부터 더하면서 N이 되면 Ok, 중간에 N이 되버리면 pass
# 시간초과..
start, end = 0, 0
cnt = 0
while end <= len(primes):
    temp_sum = sum(primes[start:end])

    if temp_sum < N:
        end +=1
    elif temp_sum == N:
        cnt += 1
        end += 1    
    else:   # 합 > N
        start += 1

print(cnt)


# 2. 통과는 했지만, 시간복잡도가 크다..
from sys import stdin

N = int(stdin.readline().rstrip())

nums = [False,False] + [True]*(N-1)
for i in range(2, int(N**0.5)+1):
    if nums[i]:
        nums[i*2::i] = [False]*((N-i)//i)

primes = []
for i in range(N+1):
    if nums[i] == True:
        primes.append(i)

cnt = 0
for i in range(len(primes)):
    for j in range(i+1, len(primes)+1):
        num = sum(primes[i:j]) 

        if num > N:
            break
        if num == N:
            cnt +=1

print(cnt)



