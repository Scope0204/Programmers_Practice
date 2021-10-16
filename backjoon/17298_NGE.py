# 크기가 N인 수열 A = A1, A2, ..., AN이 있다.
# 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오큰수는 -1

'''
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    num = i
    while num < n:
        num += 1
        if num == n:
            a[i] = -1
        elif a[num] > a[i]:
            a[i] = a[num]
            break
print(*a)
'''

# O(N^2)만큼의 시간복잡도를 해결 하기 위한 stack을 이용한 풀이
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
big = [-1] * n  # 오큰수
stack = []

stack.append(0)
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        big[stack.pop()] = a[i]
    stack.append(i)

print(*big)

# 자료구조, 스택
