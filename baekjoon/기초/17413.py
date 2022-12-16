import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0
while i < len(word):
    # 괄호
    if word[i] == "<":
        i += 1
        while word[i] != ">":
            i += 1
        i += 1
    if word[i] == "<":
        i += 1
    # 숫자 / 문자
    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        word[start:i] = word[start:i][::-1]
    # 공백
    else:
        i += 1

print("".join(word))


'''
- input
<int><max>2147483647<long long><max>9223372036854775807

- output
<int><max>7463847412<long long><max>7085774586302733229
'''
