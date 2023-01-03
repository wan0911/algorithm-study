from sys import stdin

N, K = map(int, stdin.readline().split())
cnt = 0

while True:
    if N == 1:
        break
    
    if N % K != 0:
        N -= 1
        cnt += 1
    else:
        N = N//K
        cnt += 1

print(cnt)


'''
- tc 1
25 5

- result
2

'''