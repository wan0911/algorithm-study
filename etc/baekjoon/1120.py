import sys
input = sys.stdin.readline

A, B = input().split()
min_val = 50
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1
    min_val = min(min_val, cnt)

print(min_val)