# 같은 글자(자음, 모음) 2번 연속 x / aa, ee만 허용
# 모음/자음 3개 연속 X


import re

cond1 = re.compile(r"[aeiou]")
vowels = ["a", "i", "o", "u"]

while True:
    pwd = input().rstrip()
    if pwd == "end":
        break

    check = [0] * 3
    # 조건 1
    if not cond1.search(pwd):
        check[0] += 1

    # 조건 2
    for i in range(len(pwd) - 2):
        # 모음 3연속 
        if cond1.search(pwd[i]) and cond1.search(pwd[i+1]) and cond1.search(pwd[i+2]):
            check[1] += 1
        # 자음 3연속
        elif not cond1.search(pwd[i]) and not cond1.search(pwd[i+1]) and not cond1.search(pwd[i+2]):
            check[1] += 1

    # 조건 3
    for j in range(len(pwd) - 1):
        if pwd[j] == pwd[j + 1] and (pwd[j] + pwd[j + 1]) not in ["ee", "oo"]:
            check[2] += 1

    # out
    if check[0] == 0 and check[1] == 0 and check[2] == 0:
        print("<{}> is acceptable.".format(pwd))
    else:
        print("<{}> is not acceptable.".format(pwd))



"""
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end 
"""
