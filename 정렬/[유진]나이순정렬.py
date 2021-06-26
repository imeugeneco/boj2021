# 10814 나이순 정렬
x = int(input())
users = dict()
for i in range(x):
    age, name = input().split()
    users[i] = (int(age), name)
for user in sorted(users.items(), key=lambda x: (x[1][0], x[0])):
    print(user[1][0], user[1][1]) # 65076KB, 4592ms