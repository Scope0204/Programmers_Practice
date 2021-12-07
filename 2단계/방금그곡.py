def solution(m, musicinfos):

    title = [] # 정답이 담긴 곳 

    for info in musicinfos:
        i = info.split(',')
        start = list(map(int, i[0].split(':')))
        stop = list(map(int , i[1].split(':')))
        play_time = (stop[0]*60 +stop[1]) - (start[0]*60 + start[1])
        # music_code => ~#을 한단어로 정리 후 각 코드의 배열
        music_code = []
        for code in i[3]:
            if code == "#":
                music_code[-1] = music_code[-1].lower()
            else:
                music_code.append(code)

        # m_code => ~#을 한단어로 정의한 문자열(처음에 배열로 정리 후 문자열로 통합)
        m_code = []
        for code in m:
            if code == "#":
                m_code[-1] = m_code[-1].lower()
            else:
                m_code.append(code)
        m_code = "".join(m_code)
        
        # time => 흐르는 시간 , idx => 시간에따라 music_code 추가. 초과시 0으로 다시 돌아감 
        time , idx = 0 , 0
        # answer => answer 문자열 안에 m_code가 있는지 확인  
        answer = ""

        while time != play_time:
            answer+= music_code[idx]
            if m_code in answer:
                # 일치하는 경우에는 시간과 정답을 기입
                title.append([play_time,i[2]])
                break

            if idx+1 == len(music_code):
                idx = 0
            else:
                idx += 1

            time += 1 
                    
    if title:
        # 시간을 기준으로 정렬
        # 조건없이 정렬하는 경우 시간이 같을 때 TITLE의 알파벳기준으로 정렬되기 때문에 조심
        title = sorted(title, key=lambda x: x[0] , reverse=True)
        return title[0][-1]
    
    return '(None)'
        

# print(solution("ABCDEFG" , ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABC" , ["13:50,14:00,HELLO,ABC#DEFGAB", "13:00,13:05,WORLD,AACDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"] ))


'''
다른 풀이 : 코드를 미리 정의하는법

def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]
'''