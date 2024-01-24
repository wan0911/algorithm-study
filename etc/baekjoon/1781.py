# N개 문제 -> 보상: 컵라면
# 최대 컵라면 수 -> 그리디?
# 정렬: 컵라면 수, 데드라인

# 데드라인 순으로 정렬하고, 시간 순으로 for 돌면서 가장 큰 r만 취하면

# 1. while 과 for로는 구현 실패..
from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline().rstrip())
data = [[*map(int, stdin.readline().split())] for _ in range(N)]
data.sort(key=lambda x: (x[0], -x[1]))

cnt = 0
time = 1
while len(data) > 0:
    d, r = data.pop(0)
    if d == time:
        cnt += r

    for i in range(len(data)):
        a, b = data[i]

        if a == d:
            data.pop(i)

    time += 1


print(cnt)


# 2. whlie, for론... x -> heap으로 빼는 법
from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline().rstrip())
data = [[*map(int, stdin.readline().split())] for _ in range(N)]
data.sort(key=lambda x: (x[0], -x[1]))

res = []
for d in data:
    heappush(res, d[1])
    if d[0] < len(res):
        heappop(res)

print(sum(res))



# 3. 시간 초과 풀이
# 비효율적인 로직임... 위에 방식으로 다시 암기하기
from sys import stdin

N = int(stdin.readline().rstrip())
nums = [i for i in range(1, N+1)]

primes = []
for i in range(1, N+1):
    if i < 2: continue

    is_prime = True
    for j in range(2, int(i*0.5) + 1):
        if i % j == 0:
            is_prime = False

    if is_prime:
        primes.append(i)

# 전부 연속되어야 함 -> 0번째부터 더하면서 N이 되면 Ok, 중간에 N이 되버리면 pass
cnt = 0
for i in range(len(primes)):
    for j in range(i+1, len(primes)+1):
        num = sum(primes[i:j]) 

        if num > N:
            break
        if num == N:
            cnt +=1

print(cnt)

