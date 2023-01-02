from sys import stdin

N = int(stdin.readline())
N_list = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))

def binary_search(search, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if search > N_list[mid]:
        return binary_search(search, mid + 1, end)
    elif search < N_list[mid]:
        return binary_search(search, start, mid - 1)
    else: 
        return 1
        
for i in M_list:
    print(binary_search(i, 0 , N - 1))
        
        

'''
- input
5
4 1 5 2 3
5
1 3 7 9 5

- output
1
1
0
0
1
'''