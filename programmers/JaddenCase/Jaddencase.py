def solution(s):
    answer = ''

    s = s.split(" ")
    for i in s:
        if len(i) == 0:
            answer += " "
        else:
            i = i.lower()
            i = list(i)

            i[0] = i[0].upper()
            answer += ''.join(i) + ' '

    answer = answer[:-1]
    return answer
