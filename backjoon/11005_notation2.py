system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 10진법이면 9 까지, 36진법이면 Z까지 표현된다
N, B = map(int, input().split())
answer = ''

while N != 0:
    answer += str(system[N % B])  # 위치로 진법 변환
    N //= B  # N = N//B

print(answer[::-1])


# 다른풀이
# https://dirmathfl.tistory.com/83
'''
if __name__ == "__main__": #  import 했을 때 그 모듈안에 있는 모든 코드들이 그대로 실행되는 것을 막기 위해사용
    # 참고 : https://lovelydiary.tistory.com/297
    n, b = map(int, input().split())
    answer = ''

    while n:
        r = n % b
        change_num = str(r) if r < 10 else chr(r + 55)
        answer += change_num
        # answer = change_num + answer
        n //= b

    print(answer[::-1])
'''
