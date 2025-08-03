'''
우선순위 q = (작업 번호, 요청시각, 소요시각) 
대기 큐 정렬순: 소요시간 ASC, 요청시각 ASC, 작업번호 ASC
** 요청시간 주의?
** 소요시간: 종료시간 - 요청시간
작업과 작업 사이 소요시간 = 0
[출력]
평균 작업 시간 
'''
import heapq

def solution(jobs):
    # 요청 시간순으로 정렬
    jobs.sort()
    
    wait_q = []
    curr_time, completed_jobs, tot_times = 0, 0, []
    curr_job_idx = 0
    
    while completed_jobs < len(jobs):
        # 대기 큐 생성
        # curr job idx보다 후순위 대상
        # 매번 curr_time 기준을 어떻게 처리하나 했는데
        # 1.jobs가 idx순으로 정렬되어 있음, 2.curr_time이 기준이기 때문에 현재 시간보다 더 탐색될 경우는 X
        while curr_job_idx < len(jobs) and jobs[curr_job_idx][0] <= curr_time:
            # print(curr_job_idx)
            start_t, consume_t = jobs[curr_job_idx]
            heapq.heappush(wait_q, (consume_t, start_t))
            curr_job_idx += 1
        
        if wait_q:
            consume_t, start_t = heapq.heappop(wait_q)
            curr_time += consume_t
            tot_times.append(curr_time - start_t)
            completed_jobs += 1
        else:
            curr_time = jobs[curr_job_idx][0]
    
    return sum(tot_times) // completed_jobs