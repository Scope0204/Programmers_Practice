n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
l.sort() 
s = [] 

def solution():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(n):
        s.append(l[i])
        solution();
        s.pop()

solution()    

