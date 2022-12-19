N = int(input())
code = list(input())
words = list('abcdefghijklmnopqrstuvwxyz')

result = ''
	
for i in range(0, N, 2):
	str, idx = code[i], code[i+1]
	result += words[(words.index(str) + int(idx) ** 2)%26]
	
print(result)


'''
- input
8
a1b2c3e4


- output
bflu
'''
