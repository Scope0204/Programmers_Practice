'''
m과 n보다 작거나 같은 두 자연수 x,y를 가지고
각 년도를 <x:y>형식으로 표현
이 세상의 시초의 해 = <1:1>
두번째 해 = <2:2> 
만일 x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다. 
같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1이다.
<M:N>은 그들 달력의 마지막 해로서, 이 해에 세상의 종말이 도래한다는 예언이 전해 온다. 
'''

k = int(input())
for _ in range(k):
    m,n,x,y = map(int, input().split())
    temp = True
    while (x <= m*n):
        # print(x,y,m*n)
        if x%n == y%n :
            print(x)
            temp = False
            break
        x += m
    if temp:
        print(-1)