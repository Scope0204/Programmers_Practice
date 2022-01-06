'''
1부터 n까지 자연수 중에서 중복없이 m개
수열은 오른차순
'''


# n,m = list(map(int,input().split()))
n,m = 4,3
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)

 
