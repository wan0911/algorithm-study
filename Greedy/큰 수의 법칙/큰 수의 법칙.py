from sys import stdin

N, M, K = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()

temp = [arr[-1] for _ in range(K)]
temp.append(arr[-2])

n = M//len(temp) + 1
temp = temp * n

sum = 0
for i in range(M):
    sum += temp[i]

print(sum)

'''
- tc 1
5 8 3
2 4 5 4 6

- result
46


- tc 2
5 7 2
3 4 3 4 3

- result 
28
'''