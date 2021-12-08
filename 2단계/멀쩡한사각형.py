def solution(w,h):
    answer = 1
    a,b = w,h
    
    if b>a:
        a,b = b,a
    
    while b !=0 :
        a = a%b
        a,b = b,a
    
    return w*h - (w+h-a)

print(solution(2,2))