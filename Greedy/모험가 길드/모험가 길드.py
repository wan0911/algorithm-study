from sys import stdin

N = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
data.sort()     # 오름차순 

result = 0   # 조 갯수
cnt = 0     # 현재 인원
for i in data:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
        
print(result)


'''
input
5
2 3 1 2 2

output
2
'''