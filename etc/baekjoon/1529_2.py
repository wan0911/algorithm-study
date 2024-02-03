from sys import stdin

M, N = map(int, stdin.readline().split())

prime_num = [True] * (N + 1)  # 수는 1부터 시작
prime_num[0] = False
prime_num[1] = False

# 에라토스테네스의 체
for i in range(2, int(N**0.5) + 1):
    # 배수 제거
    if prime_num[i] == True:  # 배수 제거하면서 False된 숫자는 건너뜀
        for j in range(i * 2, N + 1, i):
            prime_num[j] = False


for k in range(len(prime_num)):
    if k >= M and prime_num[k] == True:
        print(k)
