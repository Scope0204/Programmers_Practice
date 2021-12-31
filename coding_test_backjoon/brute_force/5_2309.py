a = [ int(input()) for _ in range(9)]
total = sum(a)

for i in range(9):
    for j in range(i+1,9):
        if total - (a[i]+a[j]) == 100 :
            num1, num2 = a[i], a[j]
            a.remove(num1)
            a.remove(num2)
            a.sort() # 오름차순 정리

            for ans in a:
                print(ans)
            break

    if len(a) < 9:
        break
   

