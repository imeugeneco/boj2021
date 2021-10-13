import sys, numpy as np
input = sys.stdin.readline 

n,m = list(map(int,input().split()))
map = np.array([input().strip().split() for _ in range(n)], int)
route = np.full((n,m), 0)
route[0][0] = 1
count = 0

def move(map,route,n,m, count):
	if (n+1,m+1)==map.shape:
		count += 1
		print(route)
		print("count: ", count)
		return route
	if (m<map.shape[1]-1) and (map[n][m]>map[n][m+1]): # move left
		print(f'\npos: {n},{m+1}')
		route[n][m+1] += 1
		return move(map,route,n,m+1, count)
	if (m>0) and map[n][m]>map[n][m-1]: # move right
		print(f'\npos: {n},{m-1}')
		route[n][m-1] += 1
		return move(map,route,n,m-1, count)
	if (n<map.shape[0]-1) and map[n][m]>map[n+1][m]: # move down
		print(f'\npos: {n+1},{m}')
		route[n+1][m] += 1
		return move(map,route,n+1,m, count)
		
move(map,route,0,0, count)






	