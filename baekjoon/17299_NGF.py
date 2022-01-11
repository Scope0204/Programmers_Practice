# Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때,
# Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오등큰수는 -1이다.
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
f = {}
for val in a:
    if val not in f:
        f[val] = 1
    else:
        f[val] += 1

ngf = [-1] * n  # 오등큰수
stack = []


stack.append(0)
for i in range(n):
    while stack and f[a[stack[-1]]] < f[a[i]]:
        ngf[stack.pop()] = a[i]
    stack.append(i)

    # print(a, stack, i, ngf)


print(*ngf)
