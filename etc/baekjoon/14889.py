# N = 짝수 -> 팀: 1~N
# N/2 -> 스타트 팀, 링크 팀
# i와 j가 같은 팀에 속했을 때, += Sij, Sji

# 스타트 팀, 링크 팀 능력치 차이 최소화


#  1. 최솟값 설정 때문에..!
from sys import stdin
from itertools import combinations, permutations

N = int(stdin.readline().rstrip())
nums = [i for i in range(N)]
graph = [[*map(int, stdin.readline().split())] for _ in range(N)]

start_team, link_team = 0, 0

# 4C2로 -> 스타트 팀, 링크 팀
comb = list(combinations(nums, N // 2))
comb_dict = dict()
for com in comb:
    comb_dict[com] = sum([graph[per[0]][per[1]] for per in list(permutations(com, 2))])


comb_dict = sorted(comb_dict.items())

s, e = 0, len(comb_dict) - 1
min_sum = N*N*100
while s < e:
    min_sum = min(min_sum, abs(comb_dict[s][1] - comb_dict[e][1]))
    s += 1
    e -= 1

print(min_sum)


# 2. 최솟값 설정 때문에..!
from sys import stdin
from itertools import combinations, permutations

N = int(stdin.readline().rstrip())
nums = [i for i in range(N)]
graph = [[*map(int, stdin.readline().split())] for _ in range(N)]

# 4C2로 -> 스타트 팀, 링크 팀
comb = list(combinations(nums, N // 2))
min_sum = N*N*100
for team in comb:
    other_team = list(set(nums) - set(team))  # 상대 팀
    # print(team, other_team)
    start_team_sum = sum(graph[i][j] for i, j in permutations(team, 2))
    link_team_sum = sum(graph[i][j] for i, j in permutations(other_team, 2))
    min_sum = min(min_sum, abs(start_team_sum - link_team_sum))
    
print(min_sum)

## 내가 푼건 쓰레기 코드구만...ㅋ



"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
"""

"""
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
"""
