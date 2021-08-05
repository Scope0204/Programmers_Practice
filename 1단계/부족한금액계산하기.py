def solution(price, money, count):

    sum_price = 0

    for i in range(count):
        sum_price += (i+1) * price

    return sum_price-money if money <= sum_price else 0


print(solution(3, 20, 4))

# price : 원래 이용료 , money : 현재 보유한 돈
# N번째 이용시 원래이용료의 N배를 받음
# count => 횟수

# 3, 6, 9, 12  -> 총 30
# 따라서 30 - 20 = 10 이 부족함을 return
# 부족하지 않을 시 0을 리턴. (money보다 작은 경우)
