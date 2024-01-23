# 1 종료 시간 = 2 시작 시간 ok
# 잡을 수 있는 최대 회의 수

# 완탐은 안될거고,, 정렬/우선순위일 텐데

from sys import stdin

N = int(stdin.readline().rstrip())
data = [[*map(int, stdin.readline().split())] for _ in range(N)]
data.sort(key=lambda x: (x[0], (x[1] - x[0])))

res = []
s_idx, e_idx = data.pop(0)
for s, e in data:
    if e_idx > s and (e_idx - s_idx) > (e - s):
        if len(res) > 0:
            res.pop()
        res.append([s, e])
        s_idx, e_idx = s, e

    elif s >= e_idx:
        res.append([s, e])
        s_idx, e_idx = s, e

print(len(res))


# 2. 정답

# 1 종료 시간 = 2 시작 시간 ok
# 잡을 수 있는 최대 회의 수
# 회의 시작 시간, 회의 길이 순으로 풀려 했는데.. 아닌듯..

from sys import stdin

N = int(stdin.readline().rstrip())
data = [[*map(int, stdin.readline().split())] for _ in range(N)]
data.sort(key=lambda x: (x[1], x[0]))  # 회의가 일찍 끝나는 순, 시작 순  * 시작 순도 정렬해야 순서대로 처리할 수 있음
print(data)

endtime = 0
cnt = 0
for s, e in data:
    if s >= endtime:  # 2 시작 시간 >= 1 종료 시간
        cnt += 1
        endtime = e

print(cnt)
