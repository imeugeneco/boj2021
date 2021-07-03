N = int(input())
answer = [-1] * N
answer_count = 0

def n_queen(N, answer, q_row):
    # 해를 구하면 경우의 수 + 1
    if answer[N-1] != -1:
        global answer_count 
        answer_count += 1
        return

    for q_col in range(N):
        # 첫번째 열에는 모든 위치 가능
        if q_row == 0:
            new_answer = answer.copy()
            new_answer[q_row] = q_col
            n_queen(N, new_answer, q_row+1)
        # 세로나 대각선에 퀸이 없는 위치만 가능
        else:
            if q_col in answer:
                continue
            if has_diagonal_queen(answer, q_row, q_col):
                continue
            new_answer = answer.copy()
            new_answer[q_row] = q_col
            n_queen(N, new_answer, q_row+1)

def has_diagonal_queen(answer, q_row, q_col):
    for prev_q in range(q_row):
        if abs(prev_q - q_row) == abs(answer[prev_q] - q_col):
            return True
    return False

n_queen(N, answer, 0)
print(answer_count)
