def solution(array, n):
    data = [[i, abs(i-n)] for i in array]
    data.sort(key = lambda x: (x[1], x[0]))
        
    return data[0][0]
  
 
'''
array       n   result
[3, 10, 28]	20	28
'''
