def solution(routes):
    routes.sort()
    length = len(routes)
    count = 0
    cam = [0]*length
    camera = 0
    for i in range(length-1, -1, -1):
        if cam[i] == 0:
            camera = routes[i][0]  # 진입 지점
            count += 1
        for j in range(i, -1, -1):
            # 이전 진입점(camera)이 현재 진출점보다 작거나 같다면 카메라 설치
            if cam[j] == 0 and routes[j][1] >= camera:
                cam[j] = 1  # 카메라가 구간을 커버함
    return count
