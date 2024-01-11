from sys import stdin

N = int(input())


def hanoi(num, start, to, temp):
    if num == 1:
        print(start, to)
        return

    hanoi(num - 1, start, temp, to)
    print(start, to)
    hanoi(num - 1, temp, to, start)


print(2**N - 1)
hanoi(N, 1, 3, 2)
