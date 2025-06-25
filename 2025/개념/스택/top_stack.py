# stack 으로만 구현해야 된다고 생각함 -> stack, 반복문 섞어서 풀면 될듯

top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    result = [0] * len(heights)

    while heights:
        curr = top_heights.pop()

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] >= curr:
                result[len(heights)] = i + 1
                break
        else:
            result[len(heights)] = 0

    return list(result)


print(get_receiver_top_orders(top_heights))
