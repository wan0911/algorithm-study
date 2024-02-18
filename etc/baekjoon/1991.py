# 1. 전위 순회: 루트 -> 왼쪽 -> 오른쪽
# 2. 후위 순회: 왼쪽 -> 오른쪽 -> 루트

## 기본적으로, 이진 트리는 "정렬"되어 있다
## 그래서, 왼쪽 서브트리 탐색 후, 오른쪽 서브트리 탐색을 한다고 이해하면 쉽다
## 하나의 트리 묶음 = [루트 노드, 왼쪽 노드, 오른쪽 노드]
## 그래서 하나의 트리 당 왼쪽 -> 오른쪽 -> 루트 출력 순으로 하면 됨

from sys import stdin

input = stdin.readline

N = int(input())
tree = dict()
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


# 전위 순회: 현재 노드 -> 왼쪽 노드 -> 오른쪽 노드
def preOrder(cur_node):
    if cur_node == ".":
        return

    print(cur_node, end="")

    preOrder(tree[cur_node][0]) # 왼쪽 노드
    preOrder(tree[cur_node][1]) # 오른쪽 노드


# 중위 순회: 왼쪽 노드 -> 현재 노드 -> 오른쪽 노드
def inOrder(cur_node):
    if cur_node == ".":
        return

    inOrder(tree[cur_node][0])
    print(cur_node, end="")
    inOrder(tree[cur_node][1])


# 후위 순회: 왼쪽 노드 -> 오른쪽 노드 -> 현재 노드
def postOrder(cur_node):
    if cur_node == ".":
        return

    postOrder(tree[cur_node][0])
    postOrder(tree[cur_node][1])
    print(cur_node, end="")


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')


'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''