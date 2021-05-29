def is_doom_num(num):
    return "666" in str(num)

N = int(input())
N_count = 0
doom_num = 0
num = 666
while N_count < N:
    if is_doom_num(num):
        doom_num = num
        N_count += 1
    num += 1

print(doom_num)
