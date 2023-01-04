from sys import stdin

M, N, K = map(int, stdin.readline().split())
secret_menu = ''.join(list(map(str, stdin.readline().split())))
my_menu = ''.join(list(map(str, stdin.readline().split())))

if secret_menu in my_menu: 
    print('secret')
else:
    print('normal')
    
    
'''
- tc
3 10 5 1 4 5 3 3 1 2 4 1 4 5 1 4

- result
secret
'''