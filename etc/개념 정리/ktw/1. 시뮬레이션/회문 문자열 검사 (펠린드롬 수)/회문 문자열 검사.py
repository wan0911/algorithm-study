# 펠린드롬 수?
# N <= 20 -> 완탐
# len <= 100
# 대소문자 구분 X

# 길이/2로 잘라서, reverse, 같은 글자인지

import sys

input = sys.stdin.readline

N = int(input())
words = [input().replace("\n", "") for _ in range(N)]

for i in range(N):
    word = [*map(str, words[i])]
    n = len(word) // 2

    if len(word) % 2 == 0:
        a = "".join(word[:n]).upper()
        b = "".join(list(reversed(word[n:]))).upper()
    else:
        n = len(word) // 2
        a = "".join(word[:n]).upper()
        b = "".join(list(reversed(word[n+1:]))).upper()

    if a == b:
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
