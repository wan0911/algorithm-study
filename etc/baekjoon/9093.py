import sys
num = int(sys.stdin.readline())

for _ in range(num):
    str = list(sys.stdin.readline().split())

    for i in range(len(str)):
        str[i] = str[i][::-1]
    print(' '.join(str))


'''
- input
2
I am happy today
We want to win the first prize

- result
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
'''
