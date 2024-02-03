import sys
stk1 = list(sys.stdin.readline().rstrip())
stk2 = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    # stk1 = 0 : 커서가 맨 앞
    if command[0] == "L" and stk1:
        stk2.append(stk1.pop())
    # stk2 = 0 : 커서가 끝
    elif command[0] == "D" and stk2:
        stk1.append(stk2.pop())
    elif command[0] == "B" and stk1:
        stk1.pop()
    elif command[0] == "P":
        stk1.append(command[1])

print("".join(stk1 + list(reversed(stk2))))


'''
- input
abcd
3
P x
L
P y

- output
abcdyx

'''
