from sys import stdin

N = int(stdin.readline().rstrip())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
answer = ""


def division(x, y, n):
    global answer
    check = graph[x][y]

    # 1. 구역 내 값이 모두 0/1이 아닐 때
    for i in range(x, x + n):
        for j in range(y, y + n):
            # check와 다른 색깔이 나오면, 바로 4분할 해서 함수돌리고 끝냄
            if check != graph[i][j]:
                # 각 구간에 대한 괄호를 열고 닫아줌
                answer += "("
                # 1사분면
                division(x, y, n // 2)
                # 2사분면
                division(x, y + n // 2, n // 2)
                # 3사분면
                division(x + n // 2, y, n // 2)
                # 4사분면
                division(x + n // 2, y + n // 2, n // 2)
                answer += ")"
                return

    # 2. (모든 구역 탐색 후) 구역 내 값이 모두 0/1일 때
    if check == 0:
        answer += "0"
    else:
        answer += "1"
    return


division(0, 0, N)
print(answer)
