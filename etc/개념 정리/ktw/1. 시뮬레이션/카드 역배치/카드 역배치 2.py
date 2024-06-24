import sys

input = sys.stdin.readline

card = [i + 1 for i in range(20)]

for _ in range(10):
    # 1. card[a-1, b] = card[a-1, b][::-1]
    # 2. reverse 말고, 1개씩 대치하는 법

    s, e = map(int, input().split())
    for i in range((e - s + 1 // 2)):
        card[s - 1], card[e - 1] = card[e - 1], card[s - 1]


for c in card:
    print(c, end=" ")  # end


"""
0 1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8



5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
"""
