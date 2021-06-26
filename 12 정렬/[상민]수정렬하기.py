N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

# 버블 정렬
# 각 루프마다 인접한 두 원소를 비교 후 정렬한다
# 매 루프의 마지막 요소는 정렬되므로 다음 루프에서 제외한다
def bubble_sort(nums):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
    return nums

# 개선된 버블 정렬
# 루프 중 교환이 일어나지 않으면 정렬되어 있음을 의미
# 따라서 알고리즘을 종료한다
def improved_bubble_sort(nums):
    sorted = True
    for i in range(N-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                sorted = False
        if (sorted):
            break
    return nums


# 삽입 정렬
# a[0] 부터 a[i-1]까지 정렬되어 있을 때 a[i]를 포함하여 정렬
def insertion_sort(nums):
    for i in range(N):  
        tmp = nums[i]  # 삽입할 요소
        j = i-1
        while j >= 0 and nums[j] > tmp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp
    return nums

# 선택 정렬
# 각 루프마다 최대 원소를 찾아 마지막 원소와 교환한다
# 마지막 원소는 정렬되어있으므로 다음 루프에서 제외한다
# 하나의 원소가 남을때까지 반복한다
def selection_sort(nums):
    for i in range(N-1, 0, -1):
        index = 0
        for j in range(1, i+1):
            if nums[j] > nums[index]:
                index = j
        tmp = nums[i]
        nums[i] = nums[index]
        nums[index] = tmp
    return nums



# sorted = bubble_sort(nums)
# sorted = improved_bubble_sort(nums)
# sorted = insertion_sort(nums)
sorted = selection_sort(nums)

for num in sorted:
    print(num)
