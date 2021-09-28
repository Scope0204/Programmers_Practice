import math


def solution(n, words):
    answer = []
    now = ""

    for i, v in enumerate(words):
        if i == 0:
            now = v
            answer.append(v)

        # 다음 단어(v)의 첫번째 알파벳과 현재 단어(now)가 다르거나 / 다음 단어(v) 길이가 2자리수도 안되는 경우
        # 또는 이미 나온 단어의 경우
        elif now[-1] != v[0] or len(v) < 2 or v in answer:
            # 탈락
            return [i % n+1, math.ceil((i+1)/n)]
        else:
            now = v
            answer.append(v)

    return [0, 0]


print(solution(0, 	["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(	2, ["hello", "one", "even", "never", "now", "world", "draw"]))
