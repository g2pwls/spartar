T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt_r = 0
    cnt_c = 0
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt_r += 1
            else:
                cnt_r += 0
                if cnt_r > K:
                    cnt_r = 0
                elif cnt_r == K:
                    result += 1
                    cnt_r = 0
                else:
                    cnt_r = 0
        if cnt_r > K:
            cnt_r = 0
        elif cnt_r == K:
            result += 1
            cnt_r = 0
        cnt_r = 0

    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                cnt_c += 1
            else:
                cnt_c += 0
                if cnt_c > K:
                    cnt_c = 0
                elif cnt_c == K:
                    result += 1
                    cnt_c = 0
                else:
                    cnt_c = 0
        if cnt_c > K:
            cnt_c = 0
        elif cnt_c == K:
            result += 1
            cnt_c = 0
        cnt_c = 0

    print(f"#{tc} {result}")