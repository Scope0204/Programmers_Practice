# 내 풀이 : sort 정렬을 이용한 풀이
def solution(phone_book):

    phone_book.sort()
    # 문자의 경우는 sort 정렬시 숫자를 기준으로 한다.
    # 예) 112, 21, 112122233 -> 112,112122233,21

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            # startswith()는 문자열의 앞에서부터 일치하는지 판정한다(True / False)
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
print(solution(["1", "444356", "4444", "44445"]))

# 다른풀이 : hash 정석
"""
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
"""
