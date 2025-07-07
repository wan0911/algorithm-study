shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# 1. 젤 큰 할인율 * (값 총합)
# 2. 할인율 순열 -> 반복문
# 총 할인률 계산 -> 완탐 -> 작으면 result 업데이트
# => 문제 해설 잘못함 -> 쿠폰은 1번만 사용 가능
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    result = 0

    # prices든 coupon이든 둘 중 하나만 배열 값이 없다면, 반복문을 할 필요 (x)
    # while prices:
    #     cur_price = prices.pop(0)
    #     if len(coupons) == 0 or coupons[0] == 0:
    #         result += cur_price
    #         continue
    #     cur_coupon = coupons.pop(0)
    #     result += (100 - cur_coupon) * cur_price // 100

    while prices and coupons:
        c_p = prices.pop(0)
        c_c = coupons.pop(0)
        result += (100 - c_c) * c_p // 100  # (100 - c_c) 이므로 0인 경우 고려 X

    if len(prices):
        result += sum(prices)

    return result


print(
    "정답 = 926000 / 현재 풀이 값 = ",
    get_max_discounted_price([30000, 2000, 1500000], [20, 40]),
)
print(
    "정답 = 485000 / 현재 풀이 값 = ",
    get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]),
)
print(
    "정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [])
)
print(
    "정답 = 1458000 / 현재 풀이 값 = ",
    get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]),
)
