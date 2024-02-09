array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 역순 비교
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # j보다 작은 수가 존재하면, 다음 정렬로 넘어감
            break

print(array)