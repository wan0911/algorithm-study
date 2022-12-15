## 런타임 에러

import sys

result = []

# 사전 만들기
info = []
v_info = set()
for i in range(int(sys.stdin.readline().rstrip())):
	v, w = map(int, sys.stdin.readline().split())
	info.extend([v, w, str(i+1)])
	v_info.add(v)
	

duplicated = []
for v in v_info:
	if info.count(v) > 1:
		idx = list(filter(lambda x: info[x] == v, range(len(info))))
		for i in idx:
			duplicated.append(info[i:i+3])
			duplicated.sort(key = lambda x: -x[1])
		result.append(int(duplicated[0][2]))
		duplicated.clear()
	else:
		idx = info.index(v)
		result.append(int(info[idx+2]))
	
print(sum(result))


'''
- inpuy
7
1 10
2 25
3 25
3 30
3 35
2 30
2 50


- output
13
'''
