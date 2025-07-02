# Hash(value) = *저장할 배열 길이* -> hash % 배열 = idx

# 충돌 -> 체이닝: 해쉬에서 값이 충돌할때 linkedList로 활용하는 기법
# [방법 1]
# 기존 Dict형에 value를 linkedTuple로 할당하는 것
# idx 3 충돌: dict[3] = [[k1, v1], [k2, v2], ....]
# [방법 2: open adressing 구현 x]
# 충돌 시, idx + 1... 로



