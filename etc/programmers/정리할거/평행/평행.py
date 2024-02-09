from itertools import permutations

def solution(dots):
    answer = 0
    
    def slope_calc(l1, l2):
        x1, y1 = l1
        x2, y2 = l2
        slope = (y2 - y1) / abs(x2 - x1)
        return slope
    
    data = list(permutations(dots, 2))
    slope_data = []
    for i in data:
        slope_data.append(slope_calc(i[0], i[1]))
    
    return answer
