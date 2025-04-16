# 스위치 개수 받기
N = int(input())
# 스위치 상태 받기
arr = (list(map(int, input().split())))

# 학생 수 받기
S = int(input())
for _ in range(S):
    # i: 성별, j: 받은 번호
    i, j = (map(int, input().split()))

    if i == 1: # 남학생인 경우
        # 인덱스 기준 j-1부터 끝까지인데 간격을 j만큼
        for k in range(j-1, N, j):
            # 스위치 상태 반전
            arr[k] = 1 - arr[k]

    else: # 여학생인 경우
        # 자기 번호 위치 반전
        arr[j-1] = 1 - arr[j-1]
        # 즁삼에서 거리 d만큼 퍼져가며 비교
        for d in range(1, N//2+1):
            # 제일 끝이 N보다 넘어가면 안되고, 작은 게 영보다 낮으면 안됨
            if j+d-1 >= N or j-d-1 < 0:
                break
            # 좌우 스위치가 같으면
            if arr[j+d-1] == arr[j-d-1]:
                # 스위치 상태 반전
                arr[j+d-1] = 1 - arr[j+d-1]
                arr[j-d-1] = 1 - arr[j-d-1]
            # 좌우 다르면 종료
            else:
                break

for i in range(N):
    # 줄 바꾸지 말고 한 칸 띄고 출력하기
    print(arr[i], end=' ')
    # 스위치 번호가 20의 배수일 때 
    if (i+1) % 20 == 0:
        print()