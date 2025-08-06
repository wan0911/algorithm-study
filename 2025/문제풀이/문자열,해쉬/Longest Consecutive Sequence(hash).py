class Solution(object):
    def longestConsecutive(self, nums):
        '''
        1. 해쉬 dict 만들기
            - next 숫자가 있는지 O(N)으로 확인 가능
            - 모든 num에 대해 조사 x, start 지점만 조사
        2. 
        '''
        if len(nums) == 0:
            return 0

        # 1. hash_set
        # 정렬를 하면 총 탐색 횟수는 줄일 수 있다 -> 하지먼 set은 순서 X
        hash_set = set(nums)
        
        # 2. 탐색
        max_len = 0
        for num in hash_set:
            # 이전 원소가 hash_map에 있다면 이미 탐색했다고 가정
            # "연속이 끊긴 지점"부터 탐색하니까 -> 이전 숫자가 hash_map에 없는게 맞음
            # + 여길 ans에 append해서 탐색하면 in/not ind을 찾는 데 시간복잡도가 상승
            if num - 1 not in hash_set:
                curr_len = 1
                next_num = num + 1
                while next_num in hash_set:
                    curr_len += 1
                    next_num += 1
                max_len = max(max_len, curr_len)

        return max_len