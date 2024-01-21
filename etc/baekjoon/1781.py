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
