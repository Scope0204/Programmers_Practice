def solution(n, k, bulbs):
    answer = -2
    count = 0
    b = list(bulbs)
    for i in range(n):
        if b[i] == "R":
            continue
        else:
            if i+k > len(b):
                continue
            else:
                while b[i] != "R":
                    for j in range(k):
                        if b[i+j] == "R":
                            b[i+j] = "G"
                        elif b[i+j] == "G":
                            b[i+j] = "B"
                        elif b[i+j] == "B":
                            b[i+j] = "R"
                    count += 1
    for i in b:
        if i != "R":
            return -1
    return count
print(solution(3,2,"BGG"))


'''
전구n개가 일렬로 나열
전구는 r g b 
당신은 k개의 연속된 전구를 선택해 한번에 바꿀 수 있음
r -> g
g -> b
b -> r 

전구를 벗어나게 구간 정할 수 없고 
최소한으로 눌러 모두 r로 바꿔야함

n	k	bulbs	result
6	3	"RBGRGB"	3
3	2	"BGG"	-1
4	2	"GBBG"	6

gbbg 

brbg 1
rgbg 2
rbrg 3
rrgg 4
rrbb 5
rrrr 6



'''