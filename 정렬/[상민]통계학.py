import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()


def get_average(arr):
    return round(sum(arr)/N)


def get_median(arr):
    return arr[N//2]


def get_mode(arr):
    count_dict = {}
    for i in range(-4000, 4000 + 1):
        count_dict[i] = 0

    # count frequency
    for num in arr:
        count_dict[num] += 1

    most_frequent_nums = []
    max_count = max(count_dict.values())

    # find nums with max frequency
    for i in range(-4000, 4000 + 1):
        if count_dict[i] == max_count and i not in most_frequent_nums:
            most_frequent_nums.append(i)

    if len(most_frequent_nums) >= 2:
        return most_frequent_nums[1]
    return most_frequent_nums[0]


def get_range(arr):
    return max(arr) - min(arr)


print(get_average(arr))
print(get_median(arr))
print(get_mode(arr))
print(get_range(arr))
