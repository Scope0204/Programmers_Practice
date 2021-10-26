system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
N = N[::-1]
B = int(B)

answer = 0

for i in range(len(N)):
    # print(answer, system.index(N[i]), B**i, i)
    answer += system.index(N[i]) * (B ** i)


print(answer)

# 참고 : https://growingarchive.tistory.com/208
