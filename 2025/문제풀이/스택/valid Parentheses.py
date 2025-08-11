class Solution(object):
    def isValid(self, s):
        pop_list = []
        par_dict = {"(": ")", "[": "]", "{": "}"}
        for i in range(len(s) - 1, -1, -1):
            p1 = s[i]
            if p1 in (")", "]", "}"):
                pop_list.append(p1)
            elif pop_list and par_dict[p1] == pop_list[-1]:  # 반대 괄호쌍을 만났을 때
                pop_list.pop()
            else:  # 예외 조건에 해당하는 분기처리는 else로 빼는게 좋다
                return False
        return not pop_list  # 배열 크기 말고 not을 사용하면 코드가 간단해짐


"""
class Solution(object):
    def isValid(self, s):
        # 스택: LIFO -> pop
        # 맨 위에걸 뽑는다
        # 그 다음 스택을 확인해서 유효쌍이면 
        # ({([)]})
        # [), }, ], )] [
        # ( -> ) / [ -> ] / { -> }
        # 빈 스택에 뽑아서 저장.. 닫는 괄호를 만나면 빼기
        # 일치하지 않는 괄호쌍을 만나면 break
        pop_list = []
        par_dict = {"(": ")", "[": "]", "{": "}"}
        for i in range(len(s)-1, -1, -1):
            p1 = s[i]
            if p1 in (')', ']', '}'):
                pop_list.append(p1)
            else: # 반대 괄호쌍을 만났을 때
                # print(par_dict[p1], pop_list[-1])
                if par_dict[p1] == pop_list[-1]:
                    pop_list.pop()
                else:
                    return False      
        if len(pop_list) == 0:
            return True
        else:
            return False     
"""
