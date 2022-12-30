### 유클리드 호제법

: 두 수가 서로 상대방 수를 나누어서 원하는 수를 얻는 알고리즘

: **x, y의 최대 공약수 ==  r, y의 최대 공약수** (r = x%y)

→ 반복해서 x를 y로 나누고, y에 r값을 대입하면

→ x % y == 0일 때, **y == 최대공약수**

> **1. 최대공약수(GCD)**
> 

---

: 여러 수의 공통인 약수 중, **최대**인 수

→ 큰 숫자부터 탐색 : for _ range(b, 0, -1)

: a, b가 주어질 때

→ a와 b가 서로 공약수가 있거나

→ a와 b가 서로 공약수가 없다면, 1

> **2. 최소공배수(LCM)**
> 

---

: 각각의 배수 중 공통이며, **최소**인 수

→ 작은 수 부터 탐색 : for _ range(a, (a*b)+1)

: LCM(a,b) == (a*b)//GCD(a,b)

**📌 for문** 

```python
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

```

**📌 유클리드 호제법**

```python
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
```
