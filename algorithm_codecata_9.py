# 정수 n이 주어질 때,
# n 이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해 주세요.

def solution(n):
    answer =0                # 변수를 0으로 만들어줌
    for i in range(2,n+1,2): # 2부터 n까지 짝수를 반복, 2씩 증가 하도록
        answer += i          # i값을 변수에 더해준다

    return answer