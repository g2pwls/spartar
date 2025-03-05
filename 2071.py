T = int(input())

for tc in range(1, T+1):
    # 10개의 수를 리스트로 입력 받는다.
    arr = list(map(int, input().split()))
    # 합의 값을 초기화해둔다.
    sum = 0

    # arr 리스트 안에 있는 값을 하나씩 뽑아서
    for i in arr:
        # sum에 더해준다.
        sum += i

    # 합을 리스트의 길이로 나눠준 값을 avg에 저장한다.
    avg = sum / len(arr)

    # 소숫점 첫째 자리에서 반올림해준다.
    print(f"#{tc} {avg:.0f}")