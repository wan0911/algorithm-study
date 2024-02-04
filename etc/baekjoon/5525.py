# Pn: I: N+1 개 / 0 : N개
# 문자열 S 안에, Pn이 몇 개 있는지


from sys import stdin

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()

# 1. Pn 만들고,
# 2. S에서 Pn 체크
## index 겹쳐도 됨
## 완탐이 안되려나..?

Pn = ''
for i in range(N+1):
    if i == N:
        Pn += 'I'
        break
    Pn += 'IO'
    

# I가 있는 index 잡기
# I + len(Pn) 뽑아서, Pn과 일치하는지 체크


# 1. 부분성공...
cnt = 0
for start in range(0, len(S) - len(Pn) + 1):
    # 문자열은 index 범위 초과해도 괜찮나..?
    if S[start: start + len(Pn)] == Pn:
        cnt += 1
        

print(cnt)

'''
1
13
OOIOIOIOIIOII
'''

'''
2
13
OOIOIOIOIIOII
'''