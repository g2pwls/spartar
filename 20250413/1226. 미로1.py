# 상, 하, 좌, 우 방향 이동 정의
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# bfs: 너비 우선 탐색
# maze는 미로데이터, 나머지는 시작 위치 좌표
def bfs(maze, start_y, start_x):
    # 다음 방문할 곳 위치 저장
    queue = [(start_y, start_x)]  # 리스트를 큐처럼 사용
    # visited는 이미 가봤는지 표시하는 용
    # 방문한 곳은 True로 바꿈
    visited = [[False]*16 for _ in range(16)]
    # 시작점은 이미 간 거니까 True로 표시
    visited[start_y][start_x] = True
    front = 0  # 큐에서 pop 역할을 할 인덱스

    # 큐에 더 이상 검사할 좌표가 없을 때까지 반복
    while front < len(queue):
        # 큐에서 가장 앞에 있는 좌표를 꺼냄
        y, x = queue[front]
        # front를 하나 늘려서 다음 꺼낼 위치로 이동
        front += 1

        # 지금 위치가 도착점이면 성공
        if maze[y][x] == 3:
            return 1

        # 방향 4개 검사
        for i in range(4):
            # 현재 위치에서 이동한 위치 계산
            ny = y + dy[i]
            nx = x + dx[i]

            # 미로 범위 체크
            if 0 <= ny < 16 and 0 <= nx < 16:
                # 벽이 아니고, 아직 안가본 곳이면
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    # 방문 표시함
                    visited[ny][nx] = True
                    # 다음 가야할 좌표로 큐에 넣음
                    queue.append((ny, nx))

    return 0  # 도착점 못 찾으면 실패

# 테스트케이스 10개 입력 받기
for _ in range(10):
    tc = int(input())  # 테스트 케이스 번호
    maze = [list(map(int, list(input().strip()))) for _ in range(16)]

    # 시작점 찾기
    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                start_y, start_x = y, x

    result = bfs(maze, start_y, start_x)
    print(f"#{tc} {result}")
