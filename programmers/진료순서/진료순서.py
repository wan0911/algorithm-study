def solution(emergency):
  cnt = 1
  max_val = max(emergency)
  data = [[emergency[i], i] for i in range(len(emergency))]
  data.sort(key=lambda x: (abs(max_val - x[0]), max_val-x[0]))

  for i in data:
      emergency[i[1]] = cnt
      cnt += 1

return emergency
  
  
  
# 더 나은 풀이
def solution(emergency):
    e = sorted(emergency,reverse=True)
    return [e.index(i)+1 for i in emergency]

  
'''
emergency, result
[3, 76, 24]	[3, 1, 2]
'''
