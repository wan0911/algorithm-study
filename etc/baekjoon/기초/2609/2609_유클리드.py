from sys import stdin
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


'''
- input
24 18

- output
6
72

'''
