import sys

input = sys.stdin.readline

N = int(input())
words = [input().replace("\n", "").upper() for _ in range(N)]

for i in range(N):
    word = [*map(str, words[i])]
    n = len(word) // 2
    for j in range(n):  # 단어 1개씩 비교! 역순 인덱스..!
        if word[j] != word[-1 - j]:
            print("#{} NO".format(i + 1))
            break
    else:
        print("#{} YES".format(i + 1))


"""
5
level
moon
abcba
soon
gooG
"""
