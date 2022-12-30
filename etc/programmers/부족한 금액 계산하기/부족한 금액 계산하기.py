def solution(price, money, count):
    p_sum = 0
    for i in range(1, count+1):
        p_sum += price * i
    
    if money > p_sum:
        return 0
    else:
        return p_sum - money
        
    return answer
