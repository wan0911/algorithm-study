# 수열 수 묶어서 -> 최대
# 한번만 묶을 수 있음
# 수열의 수를 모두 더함

# 오름차순 정렬, 큰 수 위주로 곱하기
# 2개씩 끊어서, 음수 체크
## 음수가 있으면 무조건 더하기

# pop으로 하면, index를 체크 안해도 됨


from sys import stdin

N = int(stdin.readline().rstrip())
nums = [int(stdin.readline().rstrip()) for _ in range(N)]

negative = []
positive = []
res = 0
while len(nums) > 0:
    num = nums.pop(0)
    if num == 1:
        res += num  # 1만 예외 경우
    elif num > 0:
        positive.append(num)
    else:
        negative.append(num)
        

positive.sort(reverse=True)
negative.sort()  

# print(negative, positive)

for i in range(0, len(negative), 2):    # negative는 0을 가장 마지막에 계산되도록..
    if i + 1 >= len(negative):
        res += negative[i]
    else:
        res += negative[i] * negative[i + 1]

for i in range(0, len(positive), 2):    # ***positive는 내림차순 정렬로 큰 수부터 계산되도록
    if i + 1 >= len(positive):
        res += positive[i]
    else:
        res += positive[i] * positive[i + 1]

print(res)



"""
4
-1
2
1
3
"""

"""
6
0
1
2
4
3
5
"""

"""
4
-2
-1
0
1
"""
