from collections import deque

# append = enqueue
# popleft = dequeue

prices = [1, 2, 3, 2, 3]


# 마지막 배열은 확인하지 않아도 됨 -> 크든 작든 1초 소요
# 배열 인덱스가 헷갈리면 상수로 넣어서 풀어본 뒤 바꾸자!
def get_price_not_fall_periods(prices):
    queue = deque(prices)
    result = []

    while queue:
        curr = queue.popleft()
        cnt = 0
        for q in queue:
            cnt += 1
            if q < curr:
                break
        result.append(cnt)
    return result


print(get_price_not_fall_periods(prices))
