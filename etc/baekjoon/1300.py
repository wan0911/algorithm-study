# 2챠원  배열 A - i, j, 1차원 배열 B - k, N*N
# B 오름차순
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)

    if temp >= K:  # 이분탐색
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
