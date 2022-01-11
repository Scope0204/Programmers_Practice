# 110111
# 2**5 2**4 2**3 2**2 2**1 2**0
# 1    1    0    1    1    1
# -32  16   -0   4    -2   1
# -13
# -13 -> 7 -> -3 -> 2 -> -1 -> 1
# 110111
import sys

n = int(sys.stdin.readline())
answer = ''
if n == 0:
    print(0)
else:
    while n != 1:
        if n % -2 != 0:
            n -= 1
            n = n//-2
            answer = '1' + answer
        else:
            n = n//-2
            answer = '0' + answer
    answer = '1' + answer
    print(answer)
