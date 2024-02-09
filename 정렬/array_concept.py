# 1. 선택 정렬
## 모든 수 비교 -> 비효율적
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min_idx]:
            array[j], array[min_idx] = array[min_idx], array[j]

print(array)


# 2. 삽입 정렬
## 필요할 때만 비교 -> 효율적
## 인덱스 i 기준으로 역순 비교
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 역순 비교
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # j보다 작은 수가 존재하면, 다음 정렬로 넘어감
            break

print(array)


# 3. 퀵 정렬
## O(NlogN)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 피벗
    tail = arr[1:]  # 피벗 제외 모든 원소

    left = [x for x in tail if x <= pivot]  # 분할(왼쪽)
    right = [x for x in tail if x > pivot]  # 분할(오른쪽)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick(left) + [pivot] + quick(right) # 재귀


print(quick(array))


# 4. 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력




# 5. 버블 정렬
a = 0
