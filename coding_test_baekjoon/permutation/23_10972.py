'''
# 순서대로 순열을 구한 코드 - 시간초과

import sys
sys.setrecursionlimit(10001)

N = int(input())
field = list(map(int, input().split()))
check = False
end = False 
answer = []

def aaa(arr):
    global check, end, answer
    if len(arr) == N:
        if check:
            end = True
            answer = arr[:]
            return
        if arr == field:
            check = True
            return

    for i in range(1,N+1):
        if not i in arr and not end:
            aaa(arr+[i])
      
aaa([])
print(-1 if answer == [] else answer)
'''

# 공식이 있는 듯 하다. c++의 next permuation모듈의 원리임

'''
주훈이 풀이

N = int(input())
field = list(map(int, input().split()))
save = -1
for i in reversed(range(1,N)):
    if field[i-1] < field[i]:
        save = i-1
        tLoc = -1
        tmp = 99999
        for j in range(save+1,N):
            if field[save] < field[j] and tmp > field[j]:
                tmp = field[j]
                tLoc = j
        field[save], field[tLoc] = field[tLoc], field[save]
        break
if not save == -1:
    tmp = field[:save+1] + sorted(field[save+1:])
    print(" ".join(list(map(str, tmp))))
    field = tmp
else:
    print(-1)

'''

'''
공식 
1. a[k] < a[k+1] 을 만족하는 값을 찾기
2. k 이후의 값 중 a[k] < a[i]을 만족하는 값 찾기
3. 있다면 해당 수와 자리를 교체해주고,  l[k+1] 부터 오름차순으로 정렬한다.

'''
n = int(input())
l = list(map(int, input().split()))

k = -1 

for i in range(n-1,0,-1):
    if l[i-1] < l[i]: # a[k] < a[k+1]
        k = i-1
        break

if k == -1: # 내림차순인 경우 (예 : 5 4 3 2 1 이 마지막임)
    print(-1)

else: 
    for i in range(n-1,0,-1):
        if l[k] < l[i]:
            l[k],l[i] = l[i],l[k]
            l = l[:k+1]+sorted(l[k+1:])        
            print(*l)
            break
    



