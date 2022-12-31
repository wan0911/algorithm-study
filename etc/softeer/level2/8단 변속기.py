from sys import stdin

order = list(map(int, stdin.readline().split()))

if order == sorted(order): print('ascending')
elif order == sorted(order, reverse = True): print('descending')
else: print('mixed')


'''
- input
1 2 3 4 5 6 7 8

- output
ascending
'''