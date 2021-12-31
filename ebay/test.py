def check(i,P):
    p = list(P) # 배열 받아옴
    answer= p[i]
    p.pop(i)
    p.pop(0) 

    while p:
        for i in range(1,len(p)):
            if p[0]+p[i] == "".join(reversed(p[0]+p[i])) or p[i]+p[0] == "".join(reversed(p[i]+p[0])): # 펠린드롭인 경우 
                p.pop(i)
                p.pop(0) 
                break
            if i == len(p)-1: #마지막인경우 
                return 0
    return answer           

   
def solution(P):
    ans = []
    for i in range(1,len(P)): # i는 p0과 매칭할 수
        a ,b = P[0] ,P[i]
        if a+b == "".join(reversed(a+b)) or b+a == "".join(reversed(b+a)): # 두 수가 펠린드롬이라면
            answer = check(i,P)
            if answer : # 이 수로 모두 없앨 수 있다면
                ans.append(answer)
            
    return ans

print(solution(["21","123","111","11"]))
'''
펠린드롬 : 앞에서나 뒤에서나 읽어도 같은 단어
문자열 n개가 들어있는 배열 p 에서
1. 임의의 두수 a,b를 뽑음
2. 두수를 붙여 펠린드롬이 되면 제거가능
3. 아니면 제거 불가
이런 식으로 모든 원소를 제거해야함
여기서 가능한 경우의 수 중 
첫번쨰 원소와 매칭되는 원소들을 리턴하는 함수를 완성
배열에 주어진 순서대로 리턴
자연수는 문자열로 주어짐 문자열은 1이상 40이하
'''