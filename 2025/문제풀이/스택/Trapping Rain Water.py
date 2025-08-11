class Solution(object):
    def trap(self, height):
        '''
        빗물 담아두기
        자기 높이 <= 다음 높이 나올 때까지 채우기
        진행방향: 오른쪽
        height[i] >= 1: elevation(벽?) 크기
        [시간] 10^4 -> 이중 반복문 X?
        [출력]
        - 빗물을 담아둔 크기
        '''

        n = len(height)
        sum_rain = 0
        stack = []
        curr_left = (0,0)

        for idx, h in enumerate(height):
            # stack 관리: 우측 벽이 커지면, 왼쪽벽이 나올 때까지 pop
            while stack and h >= stack[-1][1]:
                curr_left = stack.pop()
            # 1.왼쪽 벽 > 오른쪽 벽 -> 밧뮬 담기는 경우
            if stack: 
                left_idx, left_h = stack[0]
                min_h = min(stack, h) # 오른쪽 벽 높이(빗물이 담길 수 있는 높이)
                for j in range(left_idx + 1, idx):
                    sum_rain += max(0, min_h - height[j]) # 음수인 경우는 pass
            # 2.왼쪽 벽 < 오른쪽 벽 -> stack으로 체크, 빗물 담기는 경우
            else:
                for j in range(curr_left[0] + 1, idx):
                    # print(curr_left[1], height[idx])
                    sum_rain += (curr_left[1] - height[j])

            # default
            stack.append((idx, h))
            # print('s', stack)

        print(sum_rain)
        return sum_rain
        