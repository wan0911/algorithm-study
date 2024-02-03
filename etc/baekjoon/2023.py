from sys import stdin

N = int(stdin.readline().rstrip())
start, end = 10**(N-1), int('9'*N)

# 소수 판별 함수
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 소수 탐색
# 1. 첫 자리수 == 소수
# 2. 해당 수 * 10 + (1/3/5/7/9) 붙여가면서 소수인지 판단
# 3. 탐색 수 길이 = N이면 출력
def dfs(num):
    if len(str(num)) == N:
        print(num)
				return

    for j in range(1, 10, 2):
        next_num = num*10 + j
        if is_prime(next_num):
            dfs(next_num)

dfs(2)
dfs(3)
dfs(5)
dfs(7)