# 11)
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

def solution(num):           # evenOrOdd 라는 메서드를 쓰면 더 쉽게 가능
    if num % 2==0:
        return "Even"

    else:
        return "Odd"

# 결과 출력
print("결과 : " + solution(3))
print("결과 : " + solution(2))