from sys import stdin
from collections import defaultdict

N = stdin.readline()
order = list(map(int, stdin.readline().split()))
order.sort()

order_sum = []
order_time = 0
for i in order:
    order_time += i
    order_sum.append(order_time)

print(sum(order_sum))


'''
- input
5
3 1 4 3 2

- output
32
'''



"""더 깔끔한 풀이"""
# n = int(input())
# l = sorted(map(int,input().split()))

# t = 0
# for i in range(n):
#   t = t + (n-i)*l[i]

# print(t)