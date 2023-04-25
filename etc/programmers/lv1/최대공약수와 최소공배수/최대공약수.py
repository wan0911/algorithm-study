''' 유클리드 호제법 '''

a = 10
b = 12

# 최대공약수
for i in range(min(a,b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# 최소 공배수
for i in range(max(a,b), (a*b)+1):   # 12 ~ 120
    if i % a == 0 and i % b ==0:
        print(i)
        break
    
    
    
    
## 유클리드 호제법
x, y = map(int, stdin.readline().split())

# 최대공약수
def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

# 최소공배수
def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

print(GCD(x,y))
print(LCM(x,y))

# git용 수정