n = int(input())
measurements = list(input().split() for _ in range(n))
order = []

for person in measurements:
    x, y = int(person[0]), int(person[1])
    order.append(len([i for i in measurements if int(i[0])>x and int(i[1])>y])+1)

print(' '.join(str(i) for i in order))