# participant : 참여 선수 , completion : 완주 선수, 1명 빼고 완주
# 동명이인 있을 수 잇음

def solution(participant, completion):

    # 순서 정렬
    participant.sort()
    completion.sort()
    # 답
    answer = ""

    a = 0

    for i in participant:
        if a < len(completion) and i == completion[a]:
            a += 1  # 정렬 후 순차비교
        else:
            answer = i
            break  # 비완주자는 단 한명이므로 바로 break
    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # leo

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], [
      "josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))


# 다른 풀이
# collection 모듈 사용

"""
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""

# 다른 풀이2
# hash값은 key가 다르면 모두 다른 특징을 활용
# 수의 가감을 이용
"""
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
"""
