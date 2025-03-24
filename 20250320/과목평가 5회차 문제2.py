def traversal(i):
    global preorder_val, inorder_val, postorder_val

    # 노드번호 i가 존재 하는가?
    # i가 N보다 크면, 트리의 범위를 벗어남
    if i <= N:
        # 전위순회(현->왼->오)
        # 현재까지의 preorder_val을 2배로 키운 후, 현재 노드 값 추가
        preorder_val = preorder_val*2 + tree[i]
        # 왼쪽 자식 방문
        traversal(i * 2)

        # 중위순회(왼->현->오)
        inorder_val = inorder_val*2 + tree[i]
        # 오른쪽 자식 방문
        traversal(i * 2 + 1)

        # 후위순회(왼->오->현)
        postorder_val = postorder_val*2 + tree[i]

T = int(input())

for tc in range(1, T + 1):
    # 노드 개수
    N = int(input())
    # 완전이진트리(0번 인덱스 패딩처리)
    tree = [0] + list(map(int, input().split()))

    # 전위순회 했을때 만든 수
    preorder_val = 0
    # 후위순회 했을때 만든 수
    postorder_val = 0
    # 중위순회 했을때 만든 수
    inorder_val = 0
    # 1번부터 순회 시작
    traversal(1)
    # 답
    answer = max(preorder_val, inorder_val, postorder_val)
    print(f"#{tc} {answer}")
