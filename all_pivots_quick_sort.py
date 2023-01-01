import random


def quick(arr: list, k, j, choice):
    first = k
    last = j
    stop = k - 1
    out = last + 1
    if choice == 1:
        p = first
    elif choice == 2:
        p = last
    elif choice == 3:
        p = int((first + last) / 2)
    elif choice == 4:
        p = random.randint(first, last)
    while k <= j:
        while k < out and arr[k] <= arr[p] and k <= j:
            k = k + 1
            # print(k)
        while j > stop and arr[j] >= arr[p] and k <= j:
            j = j - 1
            # print("j=",j)
        if k < j:
            arr[k], arr[j] = arr[j], arr[k]
    if j < stop:
        j = first
    if k > out:
        k = last
    if p <= j:
        # print('first')
        arr[p], arr[j] = arr[j], arr[p]
        if j - 1 - first >= 1:
            quick(arr, first, j - 1, choice)
        if last - k >= 1:
            quick(arr, k, last, choice)
    else:
        # print("second")
        arr[p], arr[k] = arr[k], arr[p]
        if j - first >= 1:
            quick(arr, first, j, choice)
        if last - (k + 1) >= 1:
            quick(arr, k + 1, last, choice)


nums = []
for i in range(5):
    nums.append(random.randint(1,100))

print("Pivot as First")
print(nums)
quick(nums, 0, len(nums) - 1, 1)
print(nums)
print()
random.shuffle(nums)
print("Pivot as Last")
print(nums)
quick(nums, 0, len(nums) - 1, 2)
print(nums)
print()
random.shuffle(nums)
print("Pivot as Mid")
print(nums)
quick(nums, 0, len(nums) - 1, 3)
print(nums)
print()
random.shuffle(nums)
print("Pivot as Random")
print(nums)
quick(nums, 0, len(nums) - 1, 4)
print(nums)