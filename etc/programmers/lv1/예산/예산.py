def solution(d, budget):
    # budget = 10^7
    # 최대 -> greedy?
    # 1. d.sort() -> 작은 것부터 count
    # 2. cnt

    d.sort()
    cnt = 0
    for i in d:
        budget -= i
        
        if budget < 0:
            break
        else:
            cnt += 1
    
    return cnt


''' 다른 풀이 '''
## 어차피 배열 d 원소를 봐야하니까 while 대신 for문을 썼는데..
## pop을 쓰면 while로 구현 가능!

# 1. 틀림
def solution(d, budget):
    d.sort()
    cnt = 0
    sums = 0
    while budget > sums:
        sums += d.pop(0)
        cnt += 1        # 여기서 budget < sum인 경우 예외처리를 못했다.. if를 다시 쓰면 while 사용하는 의미가 없어서
    return cnt


# 2. 더 나을 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()     # sort 후, pop으로 원소를 빼주고 sum을 더 해서, if 문제 해결 가능
    return len(d)   # cnt 안 세고, 배열 길이로 계산..

'''
1. sort 정렬(greedy): 역순 -> pop 쓰기
2. cnt 말고 배열 길이로 return
'''

