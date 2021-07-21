import datetime

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


def solution(a, b):
    d = datetime.datetime(2016, a, b).weekday()
    return days[d]


print(solution(5, 24))
