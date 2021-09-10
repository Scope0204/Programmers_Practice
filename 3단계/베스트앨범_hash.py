def solution(genres, plays):
    # genres[i] : 고유번호가 i인 노래의 장르입니다.
    # plays[i] : 고유번호가 i인 노래가 재생된 횟수입니다.
    answer = []
    genre = {}

    answer2 = []

    for i in range(len(genres)):
        answer.append({"num": i, "genres": genres[i], "play": plays[i]})

        if genres[i] not in genre.keys():
            genre[genres[i]] = plays[i]
        elif genres[i] in genre.keys():
            genre[genres[i]] += plays[i]

    answer.sort(key=lambda x: x["play"], reverse=True)
    answer.sort(key=lambda x: x["genres"])

    for i in range(len(genre)):
        clear = 0
        for j in answer:
            if j["genres"] == sorted(genre.items(), key=lambda item: item[1], reverse=True)[i][0]:
                answer2.append(j["num"])
                clear += 1

            if clear == 2:
                break

    return answer2


print(solution(["classic", "pop", "classic", "classic", "pop"],
      [500, 600, 150, 800, 2500]))
print(solution(["A", "A", "B", "A", "B", "B", "A",
      "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
# 조건
"""
1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
"""
# 노래의 장르를 나타내는 문자열 배열 genres
# 노래별 재생 횟수를 나타내는 정수 배열 plays
# 앨범에 들어갈 노래의 고유 번호를 순서대로 return


# 다른 풀이 : 이중 람다

"""
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
"""
