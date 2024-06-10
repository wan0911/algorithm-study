# N개 숫자열
# s~e 중 K번째 수, 오름차순
# 완탐

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    nums = [*map(int, input().split())]
    
    temp = nums[s - 1: e]
    temp.sort()
    print("#{0} {1}".format(str(i+1), str(temp[k - 1])))
