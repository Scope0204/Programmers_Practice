# 자리를 바꾼 뒤에 해당 표에서 가장 긴 경우의 수를 체크하는 함수
def check(candy):
    n = len(candy)
    answer = 1 # 최소 한개이상이니깐
    for i in range(n):
        # row 조사
        count = 1
        for j in range(1,n):
            if candy[i][j] == candy[i][j-1] : #이전 값과 같다면
                count +=1 
            else: # 이전 값과 다르면 
                count = 1 # 초기화
            if count > answer:
                answer = count 
        
        # col조사
        count = 1
        for j in range(1,n):
            if candy[j][i] == candy[j-1][i]:
                count += 1
            else:
                count =1
            if count > answer:
                answer = count 
    # 둘 다 조사해서 가장 긴 answer 값 리턴
    return answer

# 오른쪽과 아래만 검사
n = int(input())
candy = [[ c for c in input()] for _ in range(n)]
#candy = [list(input()) for _ in range(n)]
ans = 0 

for i in range(n):
    for j in range(n):
        if j+1 < n: # row 
            # 오른쪽이랑 값 바꾸기
            candy[i][j], candy[i][j+1] = candy[i][j+1] , candy[i][j]
            check_result = check(candy)
            if check_result > ans:
                ans = check_result
            # 바꾼 값 원래대로 
            candy[i][j], candy[i][j+1] = candy[i][j+1] , candy[i][j]
        if i+1 < n: # col
            # 아래랑 값 바꾸기 
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            check_result = check(candy)
            if check_result > ans:
                ans = check_result
            # 바꾼 값 원래대로 
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(ans)