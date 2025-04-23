# N: 표의 크기
N = int(input())
# 위치를 찾을 숫자 입력
target = int(input())

# N*N 크기의 2차원 리스트 생성 모두 0으로 채우기
arr = [[0] * N  for _ in range(N)]

# 시작점 찾기
x = N // 2
y = N // 2
# 시작점 찾아서 1 넣기
arr[x][y] = 1

# 델타이동: 위쪽 -> 오른쪽 -> 아래쪽 -> 왼쪽 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 이미 1 채웠으니까 2부터 시작
num = 2
# 한 방향으로 이동할 칸 수 (처음엔 1칸)
length = 1
# 현재 이동 방향 (델타 이동 방향)
direction = 0

# 찾고자 하는 숫자 좌표 저장할 변수 (일단 중앙으로 초기화)
target_x = x
target_y = x

while num <= N * N:
    for _ in range(2):
        for _ in range(length):
            x += dx[direction]
            y += dy[direction]
            arr[x][y] = num

            # 내가 찾는 숫자면 좌표 기억
            if num == target:
                target_x = x
                target_y = y
            # 다음 숫자로 넘어가기
            num += 1
            # 숫자 다 찼으면 그만하기
            if num > N*N:
                break
        # 방향 전환
        direction = (direction+1)%4
    length += 1

for row in arr:
    # 배열 한 줄씩 출력
    print(' '.join(map(str, row)))
# 좌표 출력
print(target_x+1, target_y+1)