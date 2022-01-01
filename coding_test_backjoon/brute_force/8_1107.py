'''
버튼 0~9, + , - 
0에서 -는 변하지 않고 채널은 무한대 
이동하려는 채널 n 
최소 몇번 눌러야하는지, 현재 채널은 100번
'''
def check(num):
    num = list(str(num))
    for i in num:
        if i in m_list:
            return False
    return True

n = int(input()) # 희망채널 
m = int(input()) # 고장난 버튼
m_list = list(map(str, input().split()))

cnt = abs(n-100) 

for i in range(1000001):
    if check(i):
        cnt = min(cnt, len(str(i)) + abs(i-n))
        print(cnt)

print(cnt)





