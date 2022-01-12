n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
l.sort() 
s = [] 

def solution(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(start,n):
        s.append(l[i])
        solution(i);
        s.pop()

solution(0)    

