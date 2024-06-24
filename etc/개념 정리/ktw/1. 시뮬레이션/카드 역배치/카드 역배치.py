import sys

input = sys.stdin.readline

card = [str(i + 1) for i in range(20)]

for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    card[s, e] = reversed(card[s, e])

print(" ".join(card))   # join은 str에만 적용! int일 때 주의
