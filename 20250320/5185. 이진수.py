T = int(input())

# 16진수 -> 2진수 변환 테이블
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

for tc in range(1, T+1):
    # N: 자리수, hex_num: 16진수를 띄어쓰기 기준으로 쪼갬
    N, hex_num = input().split()
    # hex_num을 리스트로 변환해줌
    hex_num = list(hex_num)
    # 2진수 값을 저장할 빈리스트
    binary_result = []

    # hex_num 리스트 값을 for문에 하나씩 넣음
    for i in hex_num:
        # 리스트값의 2진수를 표에서 찾아서 빈리스트에 추가
        # 키를 넣으면 값을 반환
        binary_result.append(hex_to_bin[i])
    
    # 공백없이 출력
    print(f"#{tc}", ''.join(binary_result))
