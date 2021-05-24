white_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]
black_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

def main():
    board_size = 8
    N, M, full_board = getInput()
    sub_board = [row[:board_size] for row in full_board[:board_size]]
    white_count = compareBoardDifference(board_size, sub_board, white_board)
    black_count = compareBoardDifference(board_size, sub_board, black_board)
    for i in range(N-board_size+1):
        for j in range(M-board_size+1):
            sub_board = [row[j:j+board_size] for row in full_board[i:i+board_size]]
            white_count = min(compareBoardDifference(board_size, sub_board, white_board), white_count)
            black_count = min(compareBoardDifference(board_size, sub_board, black_board), black_count)
    print(min(white_count, black_count))

def getInput():
    N, M = list(map(int, input().split()))
    full_board = []
    for i in range(N):
        full_board.append(input())
    return N, M, full_board

def compareBoardDifference(board_size, board1, board2):
    count = 0
    for i in range(board_size):
        for j in range(board_size):
            if board1[i][j] != board2[i][j]:
                count += 1
    return count

main()
