'''
6 8
....*...
...**...
..*****.
...**...
....*...
........
'''

n,m = map(int , input().split())
graphs = [[0] * m for _ in range(n)]
x,y,s = [],[],[]

for i in range(n):
    line = list(input())
    for j in range(m):
        graphs[i][j] = line[j]

for col , graph in enumerate(graphs):
    for row ,val in enumerate(graph):
        size = 0
        if val == '*':
            k = 1
            while 1:
                if(col-k >=0 and col+k < n and row-k >= 0 and row+k<m):
                    size = k
                    k+= 1
                else: 
                    break

        if size > 0:
            x.append(col+1)
            y.append(row+1)
            s.append(size)

print(x,y,s)