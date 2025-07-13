from itertools import permutations


def solution(k, dungeons):
    # 순서 중요
    # 순조부 -> depth + 순열
    answer = -1
    for d in range(len(dungeons), 0, -1):
        if answer > 0:  # bactracking - dungeons 길이순으로 탐색
            break
        p_list = permutations(dungeons, d)  # 순열 조합
        for path in p_list:
            # 피로도 계산
            cur_k, cur_ans = k, 0
            for rq, rm in path:
                if cur_k < rq:
                    break
                cur_k -= rm
                # print(cur_k, rq, rm)
                cur_ans += 1
            if cur_ans > answer:
                answer = cur_ans

    return answer
