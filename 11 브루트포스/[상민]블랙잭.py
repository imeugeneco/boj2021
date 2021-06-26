N, M = list( map(int, input().split()))
N_list = list( map(int, input().split()))

answer = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            result = N_list[i] + N_list[j] + N_list[k]
            if result > answer and result <= M:
                answer = result

print(answer)
# 시간 : 124ms

