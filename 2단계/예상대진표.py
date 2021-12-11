def solution(n,a,b):
    answer = 0
    player = []
    for i in range(1,n+1):
        player.append(i)  
    
    round = 0
    win_player = []

    while 1:
        win_player= [] 
        round += 1
        for j in range(0,len(player),2):
            if player[j] == a or player[j] == b: # 처음과 다음이 정답일 때
                if player[j+1] == a or player[j+1] == b: 
                    return round # 바로 종료
                else:
                    win_player.append(player[j]) # 해당 선수 승리
            
            elif player[j+1] == a or player[j+1] == b: # 처음은 아니고 다음이 정답일 떄 
                    win_player.append(player[j+1])
                
            else:
                win_player.append(player[j])

        player = win_player   

print(solution(8,4,7))


'''
간단하게 풀 수 있으나 내 코드는 복잡하고 효율적이지 못했다

다른풀이 1 : 한줄
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

다른풀이 2 : 
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
'''