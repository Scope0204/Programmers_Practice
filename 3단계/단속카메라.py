def solution(routes):
    answer = 1
    camera = []

    for i, v in enumerate(sorted(routes)):
        if i == 0:
            camera.append(v[0])
            camera.append(v[1])
            print(camera)
        else:
            if camera[0] <= v[0] and v[0] <= camera[1]:
                camera[0] = v[0]
                if v[1] < camera[1]:
                    camera[1] = v[1]
            else:
                answer += 1
                camera[0] = v[0]
                camera[1] = v[1]

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))

# 다른풀이 :
"""
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
"""
