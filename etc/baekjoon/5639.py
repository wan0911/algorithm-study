# 이진 트리 = "정렬"
# mid 기준으로 대/소 비교 + 재귀
# 그래프 만들고, 후위순위

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 1. 배열로 풀이
preorder_arr = []
while True:
    try:
        x = int(input())
        preorder_arr.append(x)
    except:
        break


def postOrder(arr):
    # 받은 배열 길이가 0이면 return
    if len(arr) == 0:
        return

    tempL, tempR = [], []
    mid = arr[0]   # 첫번째 원소 -> 대소 비교
    
    for i in range(1, len(arr)):
        if arr[i] > mid:
            tempL = arr[1:i]
            tempR = arr[i:]
            break
    else:
        # 모두 mid보다 작은 경우
        tempL = arr[1:]

    # 전위 순위 -> tree 정렬
    postOrder(tempL)
    postOrder(tempR)
    print(mid)  # 후위 순위 출력

postOrder(preorder_arr)


# 2. 포인터로 풀이


'''
50
30
24
5
28
45
98
52
60
'''