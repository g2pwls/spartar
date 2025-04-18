def checkSudoku(M):
    for i in range(9):
        # 숫자 1~9가 한 번씩 등장했는지 체크하기 위한 배열
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            # 가로 검사
            row = M[i][j]
            # 세로 검사
            col = M[j][i]

            # 이미 사용된 숫자라면, 0을 리턴
            if row_num[row] != 0:
                return 0
            if col_num[col] != 0:
                return 0

            # 아니라면, row_num과 col_num의 각 숫자 위치를 1로 변경
            row_num[row] = 1
            col_num[col] = 1

            # 3x3 행렬 검사
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [0] * 10
                # 9개의 박스 검사
                # 3x3 크기의 행열 반복
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = M[r][c]
                        # 만약 square[num] 값이 존재하면
                        if square[num]:
                            # 0 반환
                            return 0
                        square[num] = 1

    # 반복문이 정상적으로 다 수행된다면, 올바른 스도쿠이므로 1을 리턴
    return 1


T = int(input())
for tc in range(1, T + 1):
    sdo = [list(map(int, input().split())) for _ in range(9)]

    result = checkSudoku(sdo)

    print(f"#{tc} {result}")
