from collections import deque

top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    # result = deque()  # 왼쪽부터 추가하기 위해 queue를 썼는데 아래로 변경
    result = [0] * len(heights)
    for i in range(len(top_heights) - 1, 0, -1):  # 2번째 요소까지 가므로
        for j in range(i - 1, -1, -1):
            if top_heights[j] > top_heights[i]:
                result[i] = j + 1
                break
        else:
            result[i] = 0  # 수신 못하는 경우
    return list(result)


print(get_receiver_top_orders(top_heights))


# print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

# print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders([6, 9, 5, 7, 4]))
# print(
#     "정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",
#     get_receiver_top_orders([3, 9, 9, 3, 5, 7, 2]),
# )
# print(
#     "정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",
#     get_receiver_top_orders([1, 5, 3, 6, 7, 6, 5]),
# )
