from sys import stdin

n = int(stdin.readline())
N_list = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))

def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return 1
    if len(data) == 1 and search != data[0]:
        return 0
    if len(data) == 0:
        return 0

    mid = len(data) // 2
    if search == data[mid]:
        return 1
    else:
        if search > data[mid]:
            return binary_search(data[mid + 1:], search)
        else:
            return binary_search(data[:mid], search)

for i in M_list:
    print(binary_search(N_list, i))


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