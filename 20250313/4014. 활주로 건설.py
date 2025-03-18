T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):
    N, X = map(int, input().split())  # 지도 크기, 경사로 길이
    grid = [list(map(int, input().split())) for _ in range(N)]  # 지형 정보

    def check_runway(line):
        visited = [False] * N  # 경사로 설치 여부 체크
        for i in range(N - 1):
            if line[i] == line[i + 1]:  # 높이가 같으면 통과
                continue

            if abs(line[i] - line[i + 1]) > 1:  # 높이 차이가 2 이상이면 불가능
                return False

            if line[i] > line[i + 1]:  # 내려가는 경우
                height = line[i + 1]
                for j in range(i + 1, i + 1 + X):
                    if j >= N or line[j] != height or visited[j]:
                        return False
                    visited[j] = True  # 경사로 설치

            else:  # 올라가는 경우
                height = line[i]
                for j in range(i, i - X, -1):
                    if j < 0 or line[j] != height or visited[j]:
                        return False
                    visited[j] = True  # 경사로 설치

        return True

    count = 0
    for i in range(N):
        if check_runway(grid[i]):  # 가로 방향 확인
            count += 1
        if check_runway([grid[j][i] for j in range(N)]):  # 세로 방향 확인
            count += 1

    print(f"#{t} {count}")  # 정답 출력
