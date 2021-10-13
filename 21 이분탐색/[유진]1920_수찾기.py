import sys
input = sys.stdin.readline 

#풀이 1 (시간 초과)
#n1 = int(input())
#target = sorted(list(map(int,input().split())))
#n2 = int(input())
#nums = {i:0 for i in map(int,input().split())}
#snums = sorted(nums)
#
#for num in snums:
#	for j in range(len(target)):
#		if num==target[j]:
#			nums[num]=1
#			target = target[j+1:]
#			break
#		else:
#			pass
#for i in nums.values():
#	print(i)
				
#풀이2
def search(num, target, start=0, end=None):
	if end==None:
		end = len(target)-1
	if start > end:
		return 0
	
	mid = (start+end)//2
	
	if num==target[mid]:
		return 1
	elif num>target[mid]:
		start = mid+1
	elif num<target[mid]:
		end = mid -1
	return search(num, target, start, end)
				
n1 = int(input())
target = sorted(list(map(int,input().split())))

n2 = int(input())
nums = list(map(int, input().split()))

for n in range(n2):
	print(search(nums[n], target))

# 45016KB, 924ms