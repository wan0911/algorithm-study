from sys import stdin
import re

while 1:
    pw = stdin.readline().rstrip()
    if pw == "end":
        break

    cond1 = len(re.findall("[aeiou]", pw)) != 0
    cond2 = len(re.findall("[aeiou]{3}|[^aeiou]{3}", pw)) == 0
    cond3 = len(re.findall("([a-df-np-z])\\1", pw)) == 0  # 'ee', 'oo'를 제외한 연속 문자

    if cond1 and cond2 and cond3:
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
