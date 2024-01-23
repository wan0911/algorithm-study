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

# 데드라인 != 문제 푸는 시간 -> 데드라인이 되기 전에 문제를 풀어버릴 수 있음 (ex. d=2, 1시간 만에 풀기 o)
# 문제의 총 데드라인 = max(d)
# 1 문제를 푸는 데 1시간이 소요됨

from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline().rstrip())
data = [[*map(int, stdin.readline().split())] for _ in range(N)]
data.sort(key=lambda x: (x[0], x[1]))

res = []  # 푼 문제 리스트, 즉 len(res)는 문제를 푸는데 총 걸린 시간
for d, r in data:
    heappush(res, r)  # 모든 원소들을 넣음

    if len(res) > d:  # 문제를 푼 시간(갯수)보다 데드라인이 짧을 때, data가 데드라인 순으로 정렬되있기 때문에 가능..
        heappop(res)  # 현재 들어간 문제들 중에서, 가장 작은 r(보상)을 빼냄 -> 데드라인에 한해서 최소는 계속 제거 됨

print(sum(res))
