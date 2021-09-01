def solution(clothes):

    kinds = []
    number = []
    answer = 1

    for i in clothes:
        if i[1] in kinds:
            number[kinds.index(i[1])] += 1
        else:
            kinds.append(i[1])
            number.append(1)

    for j in number:
        answer *= (j+1)

    return answer-1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["clock", "accessory"]]))


# 다른 풀이 : 공식은 같음. (의상종류+1)를 모두 곱한 후 -1
# 참고 : reduce 함수를 보면 선택적으로 initializer 를 넘길 수가 있는데, 안넘기면 lambda를 최초로 계산할 때 x에 iterable[0] 이 들어갑니다. 여기선 그렇게 되면 안되서 1 붙인 거에요
"""
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

"""
