N, M = list(map(int, input().split()))

# M 크기 순열 arr의 0번째 숫자로 1~N 사이의 숫자를 넣는다
# 재귀적으로 1~N 사이 숫자를 i번째 숫자로 넣는다
# 만약 순열이 완성되었으면 출력한다
# 루프를 돌며 1~N 사이의 모든 숫자를 넣어본다 

arr = [-1] * M
def permutation(N, M, arr, index):
    if arr[-1] != -1:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N+1):
        sub_arr = arr.copy()
        sub_arr[index] = i
        permutation(N, M, sub_arr, index+1)

permutation(N, M, arr, 0)
