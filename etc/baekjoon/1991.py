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

    preOrder(tree[cur_node][0])
    preOrder(tree[cur_node][1])


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