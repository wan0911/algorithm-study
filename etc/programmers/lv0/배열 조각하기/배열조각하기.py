def solution(arr, query):
    answer = []
    
    # query 길이만큼 반복
    ## 1. q = 짝수 or 홀수
    ## list 길이 변화 -> copy X
    ## 2. q -> slicing... pop? / 재할당
    ## 3. 예외: 배열 재할당 -> idx 문제?
    ### slicing - 범위 문제 X
    ### 인덱스 의미를 잘못 해석
    
    for i in range(len(query)):
        q = query[i]
        if i % 2 == 0:
            arr = arr[:q+1]
            
        else:
            arr = arr[q:]
        
    return arr



'''
arr	                 query	     result
[0, 1, 2, 3, 4, 5]	[4, 1, 2]	[1, 2, 3]

'''