n = int(input())

for _ in range(n):
    parenthesis = str(input())
    a = 0  # ( , ) -> ( 가 나오기 전까진 )가 나와선 안된다
    for i in parenthesis:
        if i == '(':
            a += 1
        else:
            a -= 1
            if a < 0:
                break

    if a == 0:
        print("YES")
    else:
        print("NO")

# 자료구조, 문자열, 스택
