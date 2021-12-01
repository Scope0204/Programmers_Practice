def solution(line):
    star = []
    x_list,  y_list = [],[]

    for i in range(len(line)):
        for j in range(i,len(line)):
            a,b,e = line[i]
            c,d,f = line[j]
            if i == j:
                continue
            else:
                if(a*d - b*c): # 0이 아닐때 , 두 직선이 평행이거나 일치하는게 아닐때 
                    x = (b*f-e*d) / (a*d-b*c)
                    y = (e*c-a*f) / (a*d-b*c)
                    if x.is_integer() and y.is_integer(): # 정수로만 표현되는 좌표인 경우
                        x,y = int(x),int(y)
                        star.append((x , y))
                        x_list.append(x)
                        y_list.append(y)

    max_x,min_x = max(x_list) , min(x_list)
    max_y,min_y = max(y_list) , min(y_list)
    x_size = max_x - min_x +1
    y_size = max_y - min_y +1
                       
    arr = [['.'] * x_size for _ in range(y_size)]
    for x,y in star:
        arr[max_y-y][x-min_x] = "*"

    return [''.join(s) for s in arr]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))

# 2x -y + 4 , -2x -y + 4 , 0x -y +1 , 5x -8y -12 , 5x +8y+12 
# (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4), (1.5, 1.0), (2.1, -0.19), (0, -1.5), (-2.1, -0.19), (-1.5, 1.0)
# 중 정수로만 표현되는 좌표는 (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4)

# (-1)*4 - 4*(-1) = -4 - (-4) = 0 , x = 0 
# 4*-2 - 2*4 = -8 - 8 = - 16 // 2*-1 - -1*-2  = -2 - 2 = -4 // y = -16/-4 = 4 
# (0,4)

# Ax + By + E = 0
# Cx + Dy + F = 0
# 두 직선의 교점이 유일하게 존재할 경우, 그 교점은 다음과 같습니다.

# 또, AD - BC = 0인 경우 두 직선은 평행 또는 일치합

