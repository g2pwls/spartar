N = int(input())

# 리스트 컴프리헨션
# nums = []
# for i in range(1, N+1):
#   nums.append(i)
# 처음 받을 리스트
nums = [i for i in range(1, N+1)]

# 지운 후 짝수만 받아야할 리스트
new_nums = []

# nums의 길이가 1보다 크면 계속 반복
while N > 1:
    for i in range(N):

        # 홀수번째 인덱스의 숫자들을 새 리스트에 추가
        if i % 2 == 1:
            new_nums.append(nums[i])

    # 남은 숫자들로 이루어진 리스트
    # 다음에 또 nums 에서 숫자 삭제해야하기 때문에 재정의해줌
    nums = new_nums

    # 길이 재보기기
    N = len(nums)

    # 리스트 길이가 1이면 그만
    if N == 1:
        break

print(nums[0])
