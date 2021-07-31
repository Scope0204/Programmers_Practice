# 캐시 크기에 따른 실행시간 측정 프로그램
# 캐시 교체 알고리즘은 LRU 알고리즘을 사용
# LRU : 가장 오랫동안 참조되지 않은 페이지를 교체하는 캐시 알고리즘

def solution(cacheSize, cities):

    cacheList = []
    answer = 0

    for i in cities:

        if cacheSize == 0:
            answer += 5

        elif i.lower() in cacheList:  # 있는 경우
            cacheList.pop(cacheList.index(i.lower()))  # 가장 뒤로 해당 캐쉬 이동
            cacheList.append(i.lower())
            answer += 1

        else:  # 없는 경우
            if len(cacheList) < cacheSize:
                cacheList.append(i.lower())
            else:
                cacheList.pop(0)
                cacheList.append(i.lower())
            answer += 5

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
      "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))

print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 1. cacheList에 이미 들어가 있는 경우에는 cache hit, 실행시간은 1이며 제일 뒤로 이동
# 2. cacheList는 cacheSize만큼의 킬이 만큼 들어갈 수 있다.
# 3. cacheSize만큼 다 차 있는경우에는 처음 캐시를 삭제하고 마지막으로 들어간다.
# 4. cacheSize가 0인 경우는 전부 cache miss, answer += 5


# 다른 풀이
# deque의 maxlen을 이용하여 불필요한 과정을 줄임
"""
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
"""
