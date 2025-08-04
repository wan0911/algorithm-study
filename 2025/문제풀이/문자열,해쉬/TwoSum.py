from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        해쉬로 풀어보기
        [풀이]
        1.해쉬 dict 만들기
            - 중복 key 생성되는 경우도 고려해야 함
            - dict/defaultdict/list
        2.for 반복, traget % hash 원소 -> 해쉬맵에 있는지 확인?
        """

        def hashFunction(n):
            return n % target

        # 1. 해쉬 dict 만들기 -> 그냥 전체?
        ans = []
        hash_dict = {}
        # 숫자가 중복되는 경우... -> 유효한 정답은 1개니까, 이 경우에 중복되는 숫자는 2개만 존재한다.
        for idx, num in enumerate(nums):
            if num not in hash_dict:
                hash_dict[num] = [idx]
            else:
                hash_dict[num].append(idx)
        # print(hash_dict)

        # 2. target 탐색
        for k in hash_dict.keys():
            nk = target - k
            if nk == k:
                ans = hash_dict[k]
            elif nk in hash_dict:
                ans = [hash_dict[k][0], hash_dict[nk][0]]
        
        return sorted(ans)