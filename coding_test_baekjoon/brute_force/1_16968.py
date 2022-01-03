a = input()
ans = 1

for i in range(len(a)):

    if i>0 and a[i] == a[i-1]:
        if a[i] == 'c':
            ans *= 25
        elif a[i] == 'd':
            ans *= 9
    else:
        if a[i] == 'c':
            ans *= 26
        else:
            ans *= 10

print(ans)