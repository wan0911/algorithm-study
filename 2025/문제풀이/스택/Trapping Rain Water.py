class Solution(object):
    def trap(self, height):
        n = len(height)
        
        def leftRight():
            sum_rain = 0
            stack = []
            curr_left = (0,0)
            for idx, h in enumerate(height):
                # stack 관리: 우측 벽이 커지면, 왼쪽벽이 나올 때까지 pop
                while stack and h >= stack[-1][1]:
                    curr_left = stack.pop()
                # 1.왼쪽 벽 > 오른쪽 벽 -> 밧뮬 담기는 경우
                if stack: 
                    pass
                # 2.왼쪽 벽 < 오른쪽 벽 -> stack으로 체크, 빗물 담기는 경우
                else:
                    for j in range(curr_left[0] + 1, idx):
                        sum_rain += (curr_left[1] - height[j])

                # default
                stack.append((idx, h))
            return sum_rain
        
        def rightLeft():
            sum_rain = 0
            stack = []
            curr_right = (0,0)
            for idx in range(len(height) - 1,-1,-1):
                h = height[idx]
                while stack and h > stack[0][1]:
                    curr_right = stack.pop()
                if stack: 
                    pass
                else:
                    for j in range(idx + 1, curr_right[0]):
                        sum_rain += (curr_right[1] - height[j])
                # default
                stack.append((idx, h))
            return sum_rain

        # print(leftRight())
        # print(rightLeft())
        sum1 = leftRight()
        sum2 = rightLeft()
        return sum1 + sum2