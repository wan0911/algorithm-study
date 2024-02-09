from sys import stdin

N, M = map(int, stdin.readline().split())

schedule = dict()
for _ in range(N):
    schedule[stdin.readline().rstrip()] = [0] * 10
schedule = dict(sorted(schedule.items()))

for _ in range(M):
    meeting_room, start, end = stdin.readline().split()
    for i in range(int(start), int(end)):
        schedule[meeting_room][i%9] = 1


# 출력
temp = []
for key, value in enumerate(schedule.items()):
    value[1][-1] = 1
    print(f'Room {value[0]}:')

    curr = 1
    for idx, val in enumerate(value[1]):
        idx += 9 
        if curr == 1 and val == 0:
            sTime = idx 
            curr = 0
        elif curr == 0 and val == 1:
            fTime = idx 
            curr = 1
            temp.append([sTime, fTime])
    
    if len(temp) == 0:
        print('Not available')
    else:
        print(f'{len(temp)} available:')
        for i in temp:
            print(f'{i[0]:02d}-{i[1]}')
    
    if key == len(schedule.items()) - 1:
        break
    else:
        print('-----')
        temp.clear()