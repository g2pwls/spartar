T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        a, b, c = map(int, input().split())

        for i in range(c+1):
            if 0 <= (b - 1 - i) < N and 0 <= (b - 1 + i) < N:
                if arr[b-1-i] == arr[b-1+i]:
                    arr[b-1-i] = 1 - arr[b-1-i]
                    arr[b-1+i] = 1 - arr[b-1+i]

    print(f"#{tc}", *arr)