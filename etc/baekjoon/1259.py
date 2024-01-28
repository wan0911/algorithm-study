from sys import stdin

while True:
    word = [*map(int, stdin.readline().rstrip())]
    idx = len(word) // 2

    if sum(word) == 0:
        break

    if len(word) % 2 != 0:
        word.pop(idx)

    if word[:idx] == word[len(word) : idx - 1 : -1]:
        print("yes")
    else:
        print("no")


# 다른 로직을 익히는게 좋을듯..

"""
121
1231
12421
0
"""
