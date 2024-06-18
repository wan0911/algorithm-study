import sys

input = sys.stdin.readline

N = int(input())
words = [input().replace("\n", "").upper() for _ in range(N)]

for i in range(len(words)):
    word = words[i]
    if word == word[::-1]:
        print("#{} YES".format(i + 1))
    else:
        print("#{} NO".format(i + 1))


"""
5
level
moon
abcba
soon
gooG
"""
