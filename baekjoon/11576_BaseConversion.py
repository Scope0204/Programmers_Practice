'''
1. 입력의 첫 줄에는 미래세계에서 사용하는 진법 A와 정이가 사용하는 진법 B가 공백을 구분으로 주어진다. A와 B는 모두 2이상 30이하의 자연수다.
2. 입력의 두 번째 줄에는 A진법으로 나타낸 숫자의 자리수의 개수 m(1 ≤ m ≤ 25)이 주어진다.
3. 세 번째 줄에는 A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터 차례대로 주어진다. 각 숫자는 0이상 A미만임이 보장된다. 또한 수가 0으로 시작하는 경우는 존재하지 않는다.
4. A진법으로 나타낸 수를 10진법으로 변환하였을 때의 값은 양의 정수이며 220보다 작다.

<출력>
입력으로 주어진 A진법으로 나타낸 수를 B진법으로 변환하여 출력한다.
'''

A, B = map(int, input().split())  # A진법의 수를 B진법으로
m = int(input())  # n자리수인 A진법 수
a = list(map(int, input().split()))  # A진법 수가 높은 자리수 순으로 있음
num = 0  # 10진법으로 바꾼 수
answer = []
for i in range(m):  # 10진법 계산
    num += a[i] * (A**(m-i-1))

while num:
    n = num % B  # n -> num 나누고 남은 수
    answer.append(str(n))
    num = num // B

print(' '.join(answer[::-1]))  # 자리수 마다 띄워쓰기해야함

# 풀이방법 : A진법 -> 10진법 -> B진법