'''
자연수 n m 
1부터 n까지 자연수 중에서 중복없이 m개를 고른 수열 
1 < m < n 

3 1
1부터 3까지 자연수 중에서 중복없이 3개 
1 2 3 

4 2
1 2 / 1 3 / 1 4 / 2 1 / 2 3 / 2 4 
''' 
n,m = map(int,input().split())
s = [] 
def dfs():    
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(1,n+1):
            if i not in s:
                s.append(i)
                dfs()
                s.pop()
            
dfs()