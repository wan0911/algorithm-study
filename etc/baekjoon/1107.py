# # --- 1. 틀린 풀이 ---

# # N까지 가기 위한 최소 이동 횟수 // 채널 무한대
# # 0~9 , +, - // 고장난 버튼

# # N중에서 고장난 버튼에 포함되면...
# # 재귀?
# # 1. temp 숫자 찾고, 2. +-

# from sys import stdin

# N = int(stdin.readline().rstrip())
# m = int(stdin.readline().rstrip())
# not_working_buttons = [*map(int, stdin.readline().split())]

# channels = [i for i in range(9 + 1)]
# curr_N = 100


# # 1.
# def recurrsive(n):
#     global temp, cnt

#     if n not in not_working_buttons:
#         temp += str(n)
#         cnt += 1
#         return

#     if n == 0:
#         return recurrsive(9)

#     return recurrsive(n - 1)


# # 2. temp -> N
# # 크면 - , 작으면 +... 어케 판단
# cnt = 0
# temp = ""
# for n in str(N):
#     num = int(n)
#     if num not in not_working_buttons:
#         temp += str(num)
#         cnt += 1
#     else:
#         # 재귀 / 0~9 사이에서 숫자 +-...
#         recurrsive(num)

# print(cnt, temp)


# while True:
#     temp = int(temp)
#     if temp == N:
#         break

#     if temp < N:
#         temp += 1
#     else:
#         temp -= 1

#     cnt += 1


# print(cnt, temp)

# 2.
from sys import stdin

input = stdin.readline

N = int(input().rstrip())
m = int(input().rstrip())
not_working = [*map(str, stdin.readline().split())]

# "완전탐색(브루트포스)"로 가능한 모든 경우의 수 (0~1000000)에 대해 탐색하여, 최솟값 확인

res = abs(N - 100)  # + / -로만 이동 => 최댓값

for num in range(1000001): 
    for i in str(num):
        if i in not_working:    # 해당 숫자는 눌러서 만들 수 없음
            break  

    else:  # 모든 숫자를 누를 수 있는 경우 / 여기서 else가 없으면 외부 루프의 모든 수를 검사하게 됨... 
        res = min(res, len(str(num)) + abs(num - N))  # 현재 숫자 누른 횟수 + 현재 숫자 -> target까지 가기 위해 +/- 누른 횟수

print(res)


"""
5457
3
6 7 8
"""
