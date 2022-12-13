import sys
num = int(sys.stdin.readline())

for _ in range(num):
    str = list(sys.stdin.readline())
    str.pop()
    stk = []

    if str[0] == ')':
        print('NO')
        continue

    for word in str:
        stk.append(word)
        if word == ')' and '(' in stk:
            stk.remove('(')
            stk.pop()

    if len(stk) == 0:
        print('YES')
    else:
        print('NO')


'''
- input
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

- result
NO
NO
YES
NO
YES
NO

'''
