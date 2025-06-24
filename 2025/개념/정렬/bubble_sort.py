# point
# 정렬을 하면 맨 뒷자리부터 고정됨

input = []


# 잘못된 풀이
def bubble_sort(arr):
    for i in len(arr):
        n = i
        while n < len(arr):
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]
            n += 1
    return arr


# 올바른 풀이
# 배열의 idx 기준이 아님 -> 정렬, 탐색 횟수에 초점
# 시간 복잡도: O(N^2)
def bubble_sort2(arr):
    n = len(arr)
    # arr 맨 뒷 자리를 정렬하는 횟수
    for i in range(n - 1):
        # 한번 정렳시 탐색하는 횟수
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(input)
