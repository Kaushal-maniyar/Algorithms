import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np


def merge(first, last, arr):
    mid = int((first + last) / 2)
    if last > first:
        merge(first, mid, arr)
        merge(mid + 1, last, arr)
    a1 = arr[first: mid + 1]
    a2 = arr[mid + 1: last + 1]
    k = first
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            arr[k] = a1[i]
            i = i + 1
        else:
            arr[k] = a2[j]
            j = j + 1
        k = k + 1
    while i < len(a1):
        arr[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < len(a2):
        arr[k] = a2[j]
        k = k + 1
        j = j + 1


def update_ex_merge(chunks, array):
    start = time.time()
    for i in range(chunks):
        first = int((len(array) / chunks) * i)
        last = int(first + (len(array) / chunks))
        arr = array[first:last]
        merge(0, len(arr) - 1, arr)
        filename = str(f"chunk_{i + 1}")
        file = open(filename, "w").close()
        for j in range(len(arr)):
            file = open(filename, "a")
            content = str(f"{arr[j]},")
            file.write(content)
            file.close()
    sorted_nums = []

    for i in range(len(array)):
        min_value = math.inf
        min_filename = ''
        for j in range(chunks):
            filename = str(f"chunk_{j + 1}")
            file = open(filename, 'r')
            char = file.read(1)
            number = ''
            while char != '' and char != ',':
                number = number + char
                char = file.read(1)
            file.close()
            if number != '':
                if int(number) < min_value:
                    min_value = int(number)
                    min_filename = filename
        del_str = str(min_value) + ','
        file = open(min_filename, 'r')
        temp = file.read().replace(del_str, '', 1)
        file.close()
        file = open(min_filename, 'w')
        file.write(temp)
        file.close()
        sorted_nums.append(min_value)
    end = time.time()
    print(len(sorted_nums))
    print(sorted_nums)
    return end - start


chunks = 25
nums_10 = []
nums_50 = []
nums_100 = []

for i in range(10000):
    nums_10.append(random.randint(1, 1000000))

for i in range(50000):
    nums_50.append(random.randint(1, 1000000))

for i in range(100000):
    nums_100.append(random.randint(1, 1000000))

start = time.time()
merge(0, len(nums_10) - 1, nums_10[0:])
end = time.time()
time_10 = end - start

start = time.time()
merge(0, len(nums_50) - 1, nums_50[0:])
end = time.time()
time_50 = end - start

start = time.time()
merge(0, len(nums_100) - 1, nums_100[0:])
end = time.time()
time_100 = end - start

time_ex_10 = update_ex_merge(chunks, nums_10)
time_ex_50 = update_ex_merge(chunks, nums_50)
time_ex_100 = update_ex_merge(chunks, nums_100)

print("** Time taken for different inputs by Merge Sort **")
print("Time Taken for 10,000 elements : ", time_10)
print("Time Taken for 50,000 elements : ", time_50)
print("Time Taken for 1,00,000 elements : ", time_100)

print("** Time taken for different inputs by External Merge Sort **")
print("Time Taken for 10,000 elements : ", time_ex_10)
print("Time Taken for 50,000 elements : ", time_ex_50)
print("Time Taken for 1,00,000 elements : ", time_ex_100)

x_points = np.array([10000, 50000, 100000])
y_points = np.array([time_10, time_50, time_100])
y_ex_points = np.array([time_ex_10, time_ex_50, time_ex_100])


plt.title("Time Analysis")
plt.xlabel("Input Elements")
plt.ylabel("Time in Seconds")

plt.plot(x_points, y_points, label="Merge Sort", marker='o')
plt.plot(x_points, y_ex_points, label="External Merge", marker='o')

plt.legend(loc="upper left")
plt.show()
