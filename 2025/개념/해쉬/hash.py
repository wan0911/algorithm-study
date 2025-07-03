# Hash(value) = *저장할 배열 길이* -> hash % 배열 = idx

# 충돌 -> 체이닝: 해쉬에서 값이 충돌할때 linkedList로 활용하는 기법
# [방법 1]
# 기존 Dict형에 value를 linkedTuple로 할당하는 것
# idx 3 충돌: dict[3] = [[k1, v1], [k2, v2], ....]
# [방법 2: open adressing 구현 x]
# 충돌 시, idx + 1... 로


# 1. dictonary(hash) 구현
class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        idx = hash(key) % len(self.items)  # hash와 배열 길이 -> idx
        self.items[idx] = value
        return

    def get(self, key):
        idx = hash(key) % len(self.items)
        return self.items[idx]


# 2. 충돌 -> linkedList 활용
class linkedTuple:
    def __init__(self):
        self.items = []  # linkedList 형태로 [[k, v], [k, v], ..] 형태로 구현

    def add(self, key, value):
        self.append([key, value])

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v


class linkedDict:
    def __init__(self):
        self.items = []
        for _ in range(8):
            self.items.append(linkedTuple())  # 인자를 linkdList로 할당

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        self.items[idx].put(key, value) # 여기 확인

    def get(self, key):
        idx = hash(key) % len(self.items)
        return self.items[idx].get(key)
