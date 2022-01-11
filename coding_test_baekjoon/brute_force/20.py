n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
l.sort() 
s = [] 
visit = [False] * n 

def solution(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    b = 0 

    for i in range(start, n):
        if not visit[i] and b != l[i]:
            visit[i] = True # 방문해야할 숫자의 idx를 구분한다
            s.append(l[i])
            b = l[i] # 마지막에 추가한 숫자를 기억하여 중복된 수열을 방지한다
            solution(i+1)    
            visit[i] = False 
            s.pop()


solution(0)    
