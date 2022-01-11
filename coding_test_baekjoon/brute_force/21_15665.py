n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
l.sort() 
s = [] 

def solution(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    b = 0

    for i in range(start,n):
        if b != l[i]:
            s.append(l[i])
            solution(0)
            b = l[i]
            s.pop()

solution(0)    