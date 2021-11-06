# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
# 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.
'''
# 처음풀이

n = int(input())
a = list(map(int, input().split()))
dp = [[a[0]]]

if n == 1:
    print(1)
    print(str(dp[0][0]))
else:
    for i in range(1, n):  # 첫번째는 증가하는 값이 없으니
        answer = []
        for j in range(i):
            if a[i] > a[j]:
                if a[j] not in answer:
                    answer.append(a[j])

        if a[i] not in answer:
            answer.append(a[i])
        dp.append(answer)

    # 답출력
    length, dp_list = 0, ''
    for val in dp:
        if length < len(val):
            length = len(val)
            dp_list = ' '.join(map(str, val))

print(length)
print(dp_list)
'''

# 두번째 풀이 :
''' 
1. 각 수마다 자신보다 앞에 있는 수이면서 작은 숫자들 중 가장 큰 길이를 구해 그 길이에 +1 을 해주며 -> 11053의 lis알고리즘 방식과 동일
2. 다른 배열(array) 에 그 값들을 추가해 준 뒤 출력 -> 추가된 부분
'''
n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
array = [[x] for x in a]

for i in range(n):  # 첫번째는 증가하는 값이 없으니
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            # 리스트 = 리스트 + 리스트 , 2. 값을 array 배열에 추가
            array[i] = array[j] + [a[i]]
            dp[i] = dp[j]
    dp[i] += 1  # 자기 자신보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1을 하면 된다

length, idx = 0, 0
for i in range(n):
    if length < dp[i]:
        length = dp[i]
        idx = i
print(length)
print(*array[idx])
