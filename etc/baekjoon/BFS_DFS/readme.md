> DFS / BFS

### 구현 방식
1. 인접 리스트 
    ```
    arr = [[] for n in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    ```
2. 암시적 그래프 -> 2차원 배열

### 그래프 완전 탐색
1. BFS
    - 큐(FIFO), for 반복문
    - 시간 복잡도: O(V + E)
        
2. DFS
    - 스택(LIFO), 재귀
    - 시간 복잡도: O(V + E)
