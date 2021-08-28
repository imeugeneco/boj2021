from collections import deque

N = list(map(int,input().split()))
d = N[1]
N = N[0]
ans = []
i = 0
pointer = 0
nums = deque(range(1,N+1))

while len(ans)!=N:
	if i==N-1: i = 0
	if len(nums)==1: # nums 에 하나의 숫자만 남았을 때 d가 크면 시간이 많이 소요되기 때문에 따로 예외케이스 처리함
		ans.append(str(nums.popleft()))
	else:
		pointer += 1
		if pointer==d:
			pointer = 0
			ans.append(str(nums.popleft())) # 맨 밑에서 결과물 출력할 때 join 사용했기 때문에 str로 넣어줌
		else:
			nums.append(str(nums.popleft()))
	i += 1

print("<",", ".join(ans),">",sep="")
# 32048KB, 360ms