def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        result = []
        for a, b in zip(i, j):
            result.append(a+b)
        answer.append(result)
    
    return answer


  
'''
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
'''
