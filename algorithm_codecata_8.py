# 8번)
# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.
# 각 angle이 매개변수로 주어질 때
# 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

# 예각 : 0 < angle < 90
# 직각 : angle = 90
# 둔각 : 90 < angle < 180
# 평각 : angle = 180

def solution(angle):
    if 0 < angle < 90:             # 예각일 때
        return 1                   # 1
    elif angle == 90:              # 직각일 때
        return 2                   # 2
    elif 90 < angle < 180:         # 둔각일 때
        return 3                   # 3
    elif angle == 180:             # 평각일 때
        return 4                   # 4

    # return angle                 # 필요없음/ 평각은 else만 쓰고 조건, 리턴 안써도 가능


