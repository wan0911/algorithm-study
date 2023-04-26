# 쪼개기, 2배..
import re
def solution(dartResult):
    
    temp = []
    
    cal = {'S': '**1', 'D': '**2', 'T': '**3', '*': '*2', '#': '*-1'}
    regex = r'(\d+)([SDT])([*#]?)' # 정규식
    print(re.findall(regex, dartResult))
    for idx, data in enumerate(re.findall(regex, dartResult)):
        temp.append(''.join([cal[key] if key in cal else key for key in data]))
        
        # * 이 존재하면?
        # 첫번 째면 -1 로 마지막 값 반환
        if '*' in data and idx != 0:
            temp[idx - 1] += '*2'
            
    ans = 0
    for i in temp:
        ans += eval(i)
    return ans
    
            
            
    