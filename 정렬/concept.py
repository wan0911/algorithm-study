# 1. 선택 정렬
## 모든 수 비교 -> 비효율적
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            array[j], array[min_idx] = array[min_idx], array[j]
            
print(array)




# 2. 삽입 정렬
## 필요할 때만 비교 -> 효율적
## 인덱스 i 기준으로 역순 비교
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 역순 비교
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # j보다 작은 수가 존재하면, 다음 정렬로 넘어감
            break

print(array)




# 3. 퀵 정렬
## O(NlogN)




# 4. 계수 정렬



# 5. 버블 정렬