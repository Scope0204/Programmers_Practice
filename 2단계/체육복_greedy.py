def solution(n, lost, reserve):
    reser_del = set(reserve)-set(lost)
    lost_del = set(lost)-set(reserve)

    for i in reser_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)

    return n-len(lost_del)

# level 1
# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 수업을 들을 수 있는 학생의 최댓값을 return
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다


print(solution(3, [1, 2], [2, 3]))


# 다른 풀이
# set 함수를 쓰지않은 풀이
"""
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

"""
