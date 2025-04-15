# 난쟁이 넣을 빈 리스트
heights = []
# 9번 받을거고
for _ in range(9):
  # 빈 리스트에 입력 받는대로 추가한다
  heights.append(int(input()))

# 빈리스트에 들어온 값 총합
total = sum(heights)

# 난쟁이 쌍을 한 번씩 다 비교하는 것
# 총 9번 돌릴거고
for i in range(9):
  # 바로 다음번째 난쟁이랑 비교
  # i번째와 j번째 난쟁이 골라서 키 더해보기
  for j in range(i+1, 9):
    # 총 합 키에서 난쟁이 두명 뺐을 때 값이 100이면
    if total - (heights[i] + heights[j]) == 100:
      # 가짜 난쟁이로 선언
      fake1 = heights[i]
      fake2 = heights[j]
      # 리스트에서 가짜 난쟁이 뺀다
      heights.remove(fake1)
      heights.remove(fake2)
      break
  # 만약 리스트 길이가 7이면 중단
  if len(heights)==7:
    break

# 리스트 정렬한다
heights.sort()
# 리스트값 꺼내서 프린트 한다
for h in heights:
  print(h)