a, b = map(int, input().strip().split(' '))  # a: 가로 b: 세로
for i in range(b):
    for i2 in range(a):
        if i2 == a-1:
            print("*")
        else:
            print("*", end='')


#  이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
#  별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.


# 좋은 예시
# a, b = map(int, input().strip().split(' '))
# print(("*" * a + "\n") * b)

# 새롭게 알게된 사실
# str은 print문에서 곱셈이 가능하다
