import sys
input = sys.stdin.readline

#풀이 1 (런타임 에러)
def cut_cables(cables,max_len):
	K = 0
	for cable in cables:
		K += cable//max_len
	if K==N[1]:
		print(max_len)
	elif K<N[1]:
		max_len -= 1
		cut_cables(cables,max_len)

N = list(map(int,input().split())) 
# N[0]: no. of cables, N[1]: target no.
cables = sorted(list(int(input()) for _ in range(N[0])))

tot_len = sum(cables)
max_len = tot_len//N[1]

cut_cables(cables, max_len)