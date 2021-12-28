n = int(input())
candy = [[ c for c in input()] for _ in range(n)]
candy2 = candy # 확인용 
# print(candy)
# 오른쪽과 아래만 검사
# 단 i == n-1인 경우는 오른쪽만 검사 , j == n-1인 경우는 아래만 검사

def check(i,j,i2,j2):
    a,b = candy2[i][j], candy2[i2],[j2]
    candy2[i][j] = b
    candy2[i2][j2] = a
    #여기서부터


for i,v in enumerate(candy):
    for j,v2 in v:
        if i == n-1:
           if candy[i][j] != candy[i][j+1]: # 오른쪽 검사 
               check(i,j,i,j+1)
        elif j == n-1 :
            if candy[i][j] != candy[i+1][j]: # 아래 검사
               check(i,j,i+1,j)
               
        else:
            if candy[i][j] != candy[i][j+1]: # 오른쪽 검사 
               check(i,j,i,j+1)
                
            elif candy[i][j] != candy[i+1][j]: # 아래 검사
               check(i,j,i+1,j)
                