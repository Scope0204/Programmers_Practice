n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
answer = "<"
count = 0
point = k-1

while len(people) > 1:

    count += point
    if count >= len(people):
        while count >= len(people):
            count = count-len(people)
        # print(people.pop(count))
        answer += str(people.pop(count)) + ", "
    else:
        # print(people.pop(count))
        answer += str(people.pop(count)) + ", "

answer += str(people[-1])+">"
print(answer)
