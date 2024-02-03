from sys import stdin

n = int(stdin.readline().rstrip())
scores = list(map(int, stdin.readline().split()))
max_score = max(scores)

res = []
for score in scores:
    res.append(score / max_score * 100)  
    
print(sum(res) / n)

'''
3
40 80 60
'''