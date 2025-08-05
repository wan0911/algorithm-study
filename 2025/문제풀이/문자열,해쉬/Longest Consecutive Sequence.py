class Solution(object):
    def longestConsecutive(self, nums):
        '''
        가장 긴 연속 시퀀스
        시간복잡도 O(N)
        *(제약조건 잘 보기) nums.length >= 0
        [풀이]
        1. 숫자 정렬? 
        - 숫자 중복의 경우.. set 처리? => set은 순서가 보장되지 않음 => sort 한 후 중복이면 건너뛰기로 처리
        [0, 1, 1, 2]
        2. for 반복, 다음 원소 = 현재 원소 + 1이면 temp에 추가, 더 긴 길이 치환
        [ETC]
        - 처음에 포인터 p1, p2로 접근했는데, 그러면 [0,1,1,2]인 경우 길이 처리가 어려움 -> 배열로 변경
        '''
        if not nums:
            return 0

        nums.sort()

        curr_len, max_len = 1, 1
        for idx, num in enumerate(nums): # 기준을 +1(nex) 말고 -1(prev)로 보기!
            # 중복이면 skip
            if num == nums[idx - 1]:
                continue

            if num == nums[idx - 1] + 1: # next로 보면 [0,0]인 경우는 체크 x?
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1  # 초기화 = 1 case.[0,0]

        return max_len