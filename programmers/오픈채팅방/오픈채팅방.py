def solution(record):
    answer = []
    
    data = list(map(lambda x : x.split(), record))
    update = {r[1] : r[-1] for r in data if len(r) > 2}
    
    for r in data:
        if r[0].startswith("E"):
            answer.append(f'{update.get(r[1])}님이 들어왔습니다.')
            
        elif r[0].startswith("L"):
            answer.append(f'{update[r[1]]}님이 나갔습니다.')
    return answer
  
  
  '''
  1. record
  
  ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
  
  
  2. result
  
  ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
  
  '''
