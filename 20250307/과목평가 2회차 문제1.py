T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        a, b, c = map(int, input().split())

        for i in range(b, b+c):
            if 0 <= i-1 < N:
                arr[i-1] = 1 - arr[i-1]

    print(f"#{tc}", *arr)