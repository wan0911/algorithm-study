n = int(input())

arr = []
for i in range(n):
    a, b = input().split()
    # append 시 원소 한개만!
    arr.append((a, int(b)))

## 정렬
# arr.sort(key = lambda  x: x[1])
sorted(arr, key = lambda  x: x[1])
print(arr)


## 출력
for i in range(len(arr)):
    print(arr[i][0], end=' ')
