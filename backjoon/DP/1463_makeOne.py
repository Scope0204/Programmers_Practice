# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 예) 10의 경우에 10 -> 9 -> 3 -> 1 로 3번 만에 만들 수 있다.

N = int(input())
d = [0]*(N+1)

for i in range(2, N + 1):

    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[N])

# DP
# 참고
# https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-1463-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%92%80%EC%9D%B4-Dynamic-Programming-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
