# 빈도 정렬
# 빈도순 / 먼저 나온 순

from sys import stdin
from collections import Counter

N, C = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
count = Counter(nums).most_common()
order = list(dict.fromkeys(nums))


# count 돌면서 순서대로 result에 추가하기
for i in range(len(count)):
    num, cnt = count[i]

    for j in range(i + 1, len(count)):
        if cnt == count[j][1]:  # count가 같을 때
            # order 확인
            c_ord, n_ord = order.index(num), order.index(count[j][0])

            if n_ord < c_ord:
                count[i], count[j] = count[j], count[i]

result = []
for c in count:
    a, b = c
    result.extend([c[0] for _ in range(c[1])])


print(" ".join([str(r) for r in result]))
