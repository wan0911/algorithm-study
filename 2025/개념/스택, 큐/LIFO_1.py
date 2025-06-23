# stack 활용
# 1. LIFO 특성 활용 문제
# 2. DFS 문제

# 1. 문제 해석
# 짝수
# 여는게 먼저
# => +1 ( 다음 -1 ), 마지막이 0이면 True
# 소괄호, 중괄호, 대괄호 cnt 숫자를 각각
# 가장 최근에 온 괄호가 닫히기 전까진 다른 괄호가 오면 false => LIFO
# ( ( [ { ]

# 2. 슈도 코딩
# for in s
#     if '({['
#         stack push()
#     if ')}]'
#         짝 -> stack.pop
#         짝 X -> False


def isValid(s):
    stack = []
    for f in s:
        # 여는 괄호면 그 반대 괄호를 넣음 -> 구현 편의성, 매번 반대를 체크하면 꼬이기 쉬움
        if f == "(":
            stack.append(")")
        elif f == "[":
            stack.append("]")
        elif f == "{":
            stack.append("}")
        elif not stack or stack.pop() != f:
            return False
    return not stack  # 배열의 길이를 이렇게 표현할 수 있음
