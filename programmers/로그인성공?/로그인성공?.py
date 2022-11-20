def solution(id_pw, db):
    answer = ''
    id = id_pw[0]
    pw = id_pw[1]
    
    temp = {id : pw for id, pw in db}
    
    if id in temp:
        if pw == temp[id]:
            answer = 'login'
        else: answer = 'wrong pw'
    else: answer = 'fail'        
        
    return answer
