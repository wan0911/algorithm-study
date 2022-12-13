# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
word = input()
num = int(input())
dict = []

for i in range(len(word)+1):
	for j in range(i, len(word)+1):
		if word[i:j] != '': dict.append(word[i:j])
	i += 1

dict = sorted(set(dict))
print(dict[num-1])


	
'''
- input
anmdkwnviqpanvakakzjg
10

- output
akzjg
'''
