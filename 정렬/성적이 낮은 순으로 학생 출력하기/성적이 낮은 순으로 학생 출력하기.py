from sys import stdin

N = int(stdin.readline())

list = [(stdin.readline().split()) for _ in range(N)]

list = sorted(list, key=lambda x: x[1])
print(list)


"""
2
홍길동 95
이순신 77
"""
