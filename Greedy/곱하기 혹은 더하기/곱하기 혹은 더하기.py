from sys import stdin

# 문자열 -> join (띄어쓰기)
data = list(map(int, ' '.join(stdin.readline()).split()))

new = list()
op = ['*', '+']     # +, * -> 연산자 계산
for i in range(len(data)):  
    if data[i] == 0:
        new.extend((data[i], '+'))
    else:
        new.extend((data[i], '*'))
new.pop()   # 마지막 제거
print(new)

# 인덱스 문제....... ㅠㅠ
result = 0
result += new[0]
for i in range(1, len(new), 2):
    
    if i != 0 and new[i] == '*':
        result *= new[i+1]
        
    elif i != 0 and new[i] == '+':
        result += new[i+1]

print(result)

'''
input
02984
567

output
576
210
'''

