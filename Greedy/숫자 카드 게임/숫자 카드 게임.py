from sys import stdin

N, M = map(int, stdin.readline().split())

arr = []
check = []
for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))
    check.append(min(arr[i][:]))
    
print(max(check))


## max 활용한 풀이
arr = []
result = 0
for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))
    min_value = min(arr[i][:])
    result = max(result, min_value)

print(result)

'''
- tc 1
3 3
3 1 2 
4 1 4 
2 2 2

- result
2

- tc 2
2 4
7 3 1 8
3 3 3 4

- result 
3
'''