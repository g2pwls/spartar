# 테스트케이스 개수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 2차원 리스트 저장, N개 줄 받기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 리스트 복사 지나간 자리 표기하기 위한 용도도
    visited = [[False] * N for _ in range(N)]

    # 델타 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 전체 칸을 돌면서 확인 (x:행, y:열)
    for x in range(N):
        for y in range(N):
            # 만약 해당 칸이 괴물이면
            if arr[x][y] == 2:
                # 상하좌우 하나씩 시도
                for d in range(4):
                    # 위치 이동
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 범위 지정
                    while 0 <= nx < N and 0 <= ny < N:
                        # 벽 만나면 더 이상 갈 수 없음
                        if arr[nx][ny] == 1:
                            break
                        # 아니면 광선이 지나갔다고 체크
                        visited[nx][ny] = True
                        # 같은 방향으로 계속 나아가기
                        nx += dx[d]
                        ny += dy[d]
    # 안전한 칸 변수 초기화
    safe = 0
    # 격자 다시 확인하면서
    for i in range(N):
        for j in range(N):
            # 빈칸(0)이고, 방문하지 않은 곳이면
            if arr[i][j] == 0 and not visited[i][j]:
                # 1 증가
                safe += 1

    print(f"#{tc} {safe}")

