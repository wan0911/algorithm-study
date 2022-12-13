N = int(input())
code = list(input())
words = list('a b c d e f g h i j k l m n o p q r s t u v w x y z'.replace(' ', ''))

result = ''
for i in range(N//2):
	str, idx = code[i*2:i*2+2][0], code[i*2:i*2+2][1]
	result += words[(words.index(str) + int(idx) ** 2)%26]
		
print(result)


'''
- input
8
a1b2c3e4

- output
bflu
'''
