# N개의 강의
# M개의 블루레이
# 각 블루레이 모두 같은 길이

from sys import stdin

N, M = map(int, stdin.readline().split())
records = list(map(int, stdin.readline().split()))  # 순서대로, 분 단위

# 블루레이 최소 길이? = M개가 모두 같은 길이


# 가장 큰 원소 = start (가장 많은 경우의 수)
# 모든 원소들의 합 = end (1개만 필요, 가장 작은 경우의 수)
def size():
    sum_records = 0
    cnt = 0

    for record in records:
        if sum_records + record > mid:
            cnt += 1
            sum_records = 0  # 초기화

        sum_records += record

    if sum_records > 0:  # 잔여 길이 카운트 (계속 더하다가 mid조건에 걸리지 않아 넘어온 경우)
        cnt += 1

    return cnt


start, end = max(records), sum(records)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = size()

    if count <= M:
        result = mid  # 최소 경우의 수
        end = mid - 1
    else:
        start = mid + 1

print(result)




'''
9 3
1 2 3 4 5 6 7 8 9
'''