def solution(sizes):
    wid, leng = 0

    for i, v in enumerate(sizes):
        if v[0] < v[1]:
            a, b = v[0], v[1]  # b가 큰 수
            sizes[i][0] = b  # [0]에는 큰수가 들어가도록 함(가로부분)
            sizes[i][1] = a

        if sizes[i][0] > wid:
            wid = sizes[i][0]
        if sizes[i][1] > leng:
            leng = sizes[i][1]

    return wid * leng


print(solution([[[60, 50], [30, 70], [60, 30], [80, 40]]]))

# 다른 풀이 : lambda
"""
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
"""

# 다른 풀이 : heap 알고리즘
"""
import heapq as hq

def solution(sizes):
    widths, heights = [], []
    for s in sizes:
        hq.heappush(widths, -max(s)), hq.heappush(heights, -min(s))
    return hq.heappop(widths) * hq.heappop(heights)
"""
