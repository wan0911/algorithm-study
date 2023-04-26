from itertools import product

def solution(word):
    answer = 0
    
    d = ['A', 'E', 'I', 'O', 'U']
    data = []
    for n in range(1, len(d) + 1):
         data.extend(list(map(''.join, product(d, repeat=n)))) 
            
    data = sorted(set(data))
    answer = data.index(word) + 1
    return answer
