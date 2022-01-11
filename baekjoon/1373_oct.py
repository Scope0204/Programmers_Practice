# n = input()
# count = 0
# sum = 0
# answer = ''

# for i in reversed(n):
#     sum += (2**count) * int(i)
#     if count == 2:
#         answer += str(sum)
#         count, sum = 0, 0
#     else:
#         count += 1

# if sum:
#     answer += str(sum)

# answer = list(reversed(answer))

# print(sum if sum == 0 else int(''.join(answer)))


print(oct(int(input(), 2))[2:])  # 앞에 두자리는 8진법을 나타내므로 지워준다

# print(bin(int(input(), 8))[2:]) # 2진법 -> 8진법
