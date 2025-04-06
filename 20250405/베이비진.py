T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input()))

    # 숫자들 몇번씩 나왔는지 갯수 세기
    counts = [0] * 10

    # 6개 숫자 받으니까 6번 반복
    for i in range(6):
        # 받은 숫자들을 리스트로 해서 
        i_num = nums[i]
        # 받은 숫자들의 값에 해당하는 리스트 숫자 증가
        # 숫자 등장 횟수 카운트
        counts[i_num] += 1

    # 베이비진 조건
    # run 이거나 triplet 이거나
    # run * 2 / triplet * 2 / run * 1, triplet * 1

    # run 횟수
    r_cnt = 0
    # triplet 횟수
    t_cnt = 0
    # r_cnt + t_cnt == 2 베이비진!

    # 트리플부터 판단
    # run이나 triplet이나 최대 2번이니까 2번 반복
    for j in range(2):
        # 트리플 판단
        # 숫자 10개 모두 확인
        for i in range(10):
            # 숫자 i가 등장한 횟수가 3이상이면 트리플
            if counts[i] >= 3:
                # 트리플 카운트 증가
                t_cnt += 1
                # 숫자 i 썼으니까 다음에 또 못쓰게 감소
                counts[i] -= 3

        
        # 런 판단
        # 런 시작하는 숫자는 7까지 가능
        # 012, 123, 234, ... 789
        for i in range(8):
            # 숫자가 1번이상씩 나왔으면 
            if counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
                # run 카운트 증가
                r_cnt += 1
                # 연속된 숫자 다 썼으니까 다음에 못 쓰게 감소
                counts[i] -= 1
                counts[i+1] -= 1
                counts[i+2] -= 1

    # 정답 체크 변수
    # 0이면 베이비진 불가능
    # 1이면 베이비진 가능
    answer = 0

    # 답이 되는 조건: run 개수 + triplet 개수 == 2 이면 가능
    if r_cnt + t_cnt == 2:
        answer = 1

    print(f"#{tc} {answer}")