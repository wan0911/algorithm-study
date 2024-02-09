def solution(n):
    
    def fac(num):
        if num <= 1:
            return 1
        return num * fac(num - 1)
    
    i = 0
    while True:
        i += 1
        if fac(i) > n: return i - 1

    return i

