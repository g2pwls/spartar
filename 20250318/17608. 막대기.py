N = int(input())
# 숫자 받아와서 리스트에 다 추가하기
arr = []

for _ in range(N):
    h = int(input())
    arr.append(h)

    # 맨 오른쪽값 본인은 항상 포함이기 때문에 1로 지정
    cnt = 1
    # 가장 큰 높이를 맨 오른쪽으로 지정
    max_height = arr[-1]

# 인덱스 기준으로 맨 오른쪽껀 보이니까 그거 빼고
# 하나 앞인 인덱스 4번부터 비교해야하기 때문에
# N-2부터 0번까지 -1해서 비교
for i in range(N-2, -1, -1):
    # 맨 오른쪽 보다 더 큰 리스트 값이 있으면
    if arr[i] > max_height:
        # 카운트 1 증가
        cnt += 1
        # 가장 큰 높이를 변경
        max_height = arr[i]

print(cnt)

