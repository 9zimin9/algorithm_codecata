# 13)
# 자연수 N이 주어 지면, N의 각 자릿 수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를 들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(n):
    answer = 0
    str_n = str(n)    # n을 문자열로 변환

    for i in range(len(str_n)):
        answer += int(str_n[i])   # n_str의 i번째 문자(각 자릿수 다)를 정수로 바꾸어 answer에 더해줌



    return answer

# 실행해보기
print(solution(12345))  # 출력: 15