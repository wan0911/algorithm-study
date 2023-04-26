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