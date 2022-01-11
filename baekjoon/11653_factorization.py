n = int(input())

if n != 1:
    while n > 1:
        count = 2
        if n % count != 0:
            while n % count != 0:
                count += 1

        print(count)
        n //= count
