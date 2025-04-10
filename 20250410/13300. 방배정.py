# N: 학생수, K: 한 방에 들어갈 수 있는 인원 수
N, K = map(int, input().split())
# 성별과 학년으로 나누기 위한 2차원 배열
# students[성별][학년] 형태로 저장
students = [[0]*6 for _ in range(2)]

# N명의 학생 정보를 입력 받음
for _ in range(N):
    # S: 성별, Y: 학년
    S, Y = map(int, input().split())
    # 해당 성별, 학생 수 하나 증가
    students[S][Y-1] += 1

# 필요한 방 수를 세기 위한 변수
room_count = 0

# 성별, 학년 조합 확인하기
for gender in range(2):
    for grade in range(6):
        # 조합된 학생 수
        count = students[gender][grade]
        # 같은 성별, 같은 학년인 학생 수 // 한 방에 들어갈 수 있는 학생 수 몫
        room_count += count // K
        # 만약 나머지가 있으면
        if count % K:
            # 방 개수 하나 더 추가
            room_count += 1

print(room_count)