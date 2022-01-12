n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
# n,m = 4,2
# l = [9,7,9,1]
l.sort() 
s = [] 
visit = [False] * n 

def solution():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    b = 0 

    for i in range(n):
        if not visit[i] and b != l[i]:
            visit[i] = True # 방문해야할 숫자의 idx를 구분한다
            s.append(l[i])
            b = l[i] # 마지막에 추가한 숫자를 기억하여 중복된 수열을 방지한다
            solution()    
            visit[i] = False 
            s.pop()


solution()    
