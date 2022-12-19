a = 10
b = 12

# 최대공약수
for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        break

# 최소 공배수
# 12 ~ 120
for i in range(max(a,b), (a*b)+1):
    if i%a == 0 and i%b ==0:
        print(i)
        break
