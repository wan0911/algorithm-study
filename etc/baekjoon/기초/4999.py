import sys

input = sys.stdin.readline

A = input()
B = input()

if len(A) >= len(B):
    print("go")
else:
    print("no")
