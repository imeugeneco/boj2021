# 1181 단어 정렬
x = int(input())
words = set(input() for _ in range(x))
res = sorted(words, key=lambda x: (len(x), str(x)))
for i in res:
	print(i)