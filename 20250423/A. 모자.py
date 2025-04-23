T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    cnt = 0
    cnt_res = 0

    for i in range(N):
        for j in range(N):
            if abs(arr[i] - brr[j]) <= 3:
                cnt += 1

        if cnt > 0:
            cnt_res += 1
            cnt = 0

    print(f"#{tc} {cnt_res}")