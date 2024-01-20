# 힙 사용

# 1. 메모리.. 효율적이지 않음
from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline().rstrip())

scores = []
for _ in range(N):
    n = float(stdin.readline().rstrip())
    heappush(scores, n)

for _ in range(7):
    print("{:.3f}".format(heappop(scores)))


# 2. 힙만 사용하지 말고, 로직을 추가하는게 좋음
from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline().rstrip())

scores = [-float("inf")] * 7

for _ in range(N):
    n = float(stdin.readline().rstrip())

    if scores[0] < -n:  # heap쓴다고 정렬되는건 x, 기본 = 최소 힙
        heappop(scores)
        heappush(scores, -n)

scores.sort(reverse=True)  # 마지막에 한번만 정렬
for s in scores:
    print("{:.3f}".format(-s))


## 근데 아래처럼 sort 써도 속도랑 메모리 사용량은 비슷한듯...
from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline().rstrip())

scores = [float("inf")] * 7

for _ in range(N):
    n = float(stdin.readline().rstrip())

    if scores[6] > n:
        scores.pop()
        heappush(scores, n)
        scores.sort()

for _ in range(7):
    print("{:.3f}".format(heappop(scores)))
