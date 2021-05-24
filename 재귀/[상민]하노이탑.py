moves = []
def hanoi(n, src, mid, dest):
    if n == 1:
        moves.append(f"{src} {dest}")
    else:
        hanoi(n-1, src, dest, mid)
        hanoi(1, src, mid, dest)
        hanoi(n-1, mid, src, dest)

n = int(input())
hanoi(n, 1, 2, 3)
print(len(moves))
for move in moves:
    print(move)
