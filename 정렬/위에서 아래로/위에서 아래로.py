from sys import stdin

N = int(stdin.readline())
list = [int(stdin.readline()) for _ in range(N)]

list.sort(reverse=True)
print(list)


"""
3
15
27
2
"""
