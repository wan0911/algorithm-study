# 완전 탐색 -> 모든 경우의 수
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 순열 - 순서
    for case in permutations(dungeons, len(dungeons)):        
        
        result, curr = 0, k
        for need, fatigue in case:
            if curr >= need:
                curr -= fatigue
                result += 1
            else:
                break
        answer = max(answer, result)
    
    return answer
