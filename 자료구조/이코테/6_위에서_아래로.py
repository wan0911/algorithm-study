# 선택정렬
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]  # 스와프

print(array)
