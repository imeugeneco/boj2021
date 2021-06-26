N = int(input())
weight_height_list = []
for i in range(N):
    weight_height_list.append(list(map(int, input().split())))
answer = []

for i in range(N):
    rank = 1
    weight, height = weight_height_list[i]
    for j in range(N):
        cmp_wegith, cmp_height = weight_height_list[j]
        if weight < cmp_wegith and height < cmp_height:
            rank += 1
    answer.append(rank)

answer = list(map(str, answer))
print(' '.join(answer))
