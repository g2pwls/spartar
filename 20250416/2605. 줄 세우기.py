# 학생 수 입력
N = int(input())
# 학생이 뽑은 번호 리스트로 받기
num = list(map(int, input().split()))

# 학생 줄 다시 만들기 위한 빈리스트
line = []

# 학생 수만큼 반복할건데
for i in range(N):
    # 학생 번호 - 뽑은 번호 = 넣는 위치, i+1 = 넣을 번호
    line.insert(i-num[i], i+1)

# 리스트 출력
print(*line)
# print(' '.join(map(str, line)))