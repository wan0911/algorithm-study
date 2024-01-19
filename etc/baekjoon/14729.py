# 7명 제외 = 성적 낮은 순(오름차순) = 칠무해
## 성적 무작위 입력, 동점자 제외 = 그냥 순서대로
# N이 커서 전체를 정렬하면 안됨 -> 정렬.. / 힙

from sys import stdin

N = int(stdin.readline().rstrip())
scores = [float(stdin.readline().rstrip()) for _ in range(7)]  # 7개만 뽑아옴
scores.sort()

for _ in range(N - 7):  # 나머지 입력
    num = float(stdin.readline().rstrip())
    if scores[6] > num:
        scores.pop()
        scores.append(num)
    scores.sort()  # 7개만 정렬하면 됨.. (전체 정렬 x)

for sc in scores:
    print("%.3f" % (sc))


"""
8
20.000
70.000
50.000
30.000
70.000
30.000
60.000
70.000
"""
