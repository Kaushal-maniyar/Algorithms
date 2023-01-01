import random
import time
import matplotlib.pyplot as plt
import numpy as np


def insertion(arr):
    for k in range(1, len(arr)):
        key = arr[k]
        j = k - 1
        while j >= 0 and key <= arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


def bubble(arr):
    for k in range(len(arr) - 1):
        no_swap = True
        for j in range(0, len(arr) - k - 1):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                no_swap = False
        if no_swap:
            break


def selection(arr):
    change = False
    for k in range(len(arr)):
        small = k
        for j in range(k + 1, len(arr)):
            if arr[j] <= arr[small]:
                small = j
                change = True
        if change:
            arr[k], arr[small] = arr[small], arr[k]


def quick(arr: list):
    if len(arr) >= 2:
        p = 0
        k = p + 1
        j = arr.index(arr[-1])
        last = j + 1
        while k <= j:
            while arr[k] <= arr[p] and k <= last and k <= j:
                k = k + 1
                if k == last:
                    break
            while arr[j] >= arr[p] and j >= p and k <= j:
                j = j - 1
            if k <= j:
                arr[k], arr[j] = arr[j], arr[k]
        arr[p], arr[j] = arr[j], arr[p]
        return quick(arr[:j]) + [arr[j]] + quick(arr[k:])
    else:
        return arr


nums_10 = []
nums_50 = []
nums_100 = []

for i in range(10000):
    nums_10.append(random.randint(1, 1000000))

for i in range(50000):
    nums_50.append(random.randint(1, 1000000))

for i in range(100000):
    nums_100.append(random.randint(1, 1000000))

# 10,000 random insertion
start = time.process_time()
insertion(nums_10)
end = time.process_time()
in_ran_time_10 = end - start
print("in_ran_10 done")
print(in_ran_time_10)

# 50,000 random insertion
start = time.process_time()
insertion(nums_50)
end = time.process_time()
in_ran_time_50 = end - start
print("in_ran_50 done")
print(in_ran_time_50)

# 1,00,000 random insertion
start = time.process_time()
insertion(nums_100)
end = time.process_time()
in_ran_time_100 = end - start
print("in_ran_100 done")
print(in_ran_time_100)

# Shuffling
random.shuffle(nums_10)
random.shuffle(nums_50)
random.shuffle(nums_100)

# 10,000 random bubble
start = time.process_time()
bubble(nums_10)
end = time.process_time()
bu_ran_time_10 = end - start
print("bu_ran_10 done")
print(bu_ran_time_10)

# 50,000 random bubble
start = time.process_time()
bubble(nums_50)
end = time.process_time()
bu_ran_time_50 = end - start
print("bu_ran_50 done")
print(bu_ran_time_50)

# 1,00,000 random bubble
start = time.process_time()
bubble(nums_100)
end = time.process_time()
bu_ran_time_100 = end - start
print("bu_ran_100 done")
print(bu_ran_time_100)

# Shuffling
random.shuffle(nums_10)
random.shuffle(nums_50)
random.shuffle(nums_100)

# 10,000 random selection
start = time.process_time()
selection(nums_10)
end = time.process_time()
se_ran_time_10 = end - start
print("se_ran_10 done")
print(se_ran_time_10)

# 50,000 random selection
start = time.process_time()
selection(nums_50)
end = time.process_time()
se_ran_time_50 = end - start
print("se_ran_50 done")
print(se_ran_time_50)

# 1,00,000 random selection
start = time.process_time()
selection(nums_100)
end = time.process_time()
se_ran_time_100 = end - start
print("se_ran_100 done")
print(se_ran_time_100)

# Shuffling
random.shuffle(nums_10)
random.shuffle(nums_50)
random.shuffle(nums_100)

# 10,000 random quick
start = time.process_time()
quick(nums_10)
end = time.process_time()
qu_ran_time_10 = end - start
print("qu_ran_10 done")
print(qu_ran_time_10)

# 50,000 random quick
start = time.process_time()
quick(nums_50)
end = time.process_time()
qu_ran_time_50 = end - start
print("qu_ran_50 done")
print(qu_ran_time_50)

# 1,00,000 random quick
start = time.process_time()
quick(nums_100)
end = time.process_time()
qu_ran_time_100 = end - start
print("qu_ran_100 done")
print(qu_ran_time_100)

# Sort the array
nums_10.sort()
nums_50.sort()
nums_100.sort()

# 10,000 increasing insertion
start = time.process_time()
insertion(nums_10)
end = time.process_time()
in_in_time_10 = end - start
print("in_in_10 done")
print(in_in_time_10)

# 50,000 increasing insertion
start = time.process_time()
insertion(nums_50)
end = time.process_time()
in_in_time_50 = end - start
print("in_in_50 done")
print(in_in_time_50)

# 1,00,000 increasing insertion
start = time.process_time()
insertion(nums_100)
end = time.process_time()
in_in_time_100 = end - start
print("in_in_100 done")
print(in_in_time_100)

# 10,000 increasing bubble
start = time.process_time()
bubble(nums_10)
end = time.process_time()
bu_in_time_10 = end - start
print("bu_in_10 done")
print(bu_in_time_10)

# 50,000 increasing bubble
start = time.process_time()
bubble(nums_50)
end = time.process_time()
bu_in_time_50 = end - start
print("bu_in_50 done")
print(bu_in_time_50)

# 1,00,000 increasing bubble
start = time.process_time()
bubble(nums_100)
end = time.process_time()
bu_in_time_100 = end - start
print("bu_in_100 done")
print(bu_in_time_100)

# 10,000 increasing selection
start = time.process_time()
selection(nums_10)
end = time.process_time()
se_in_time_10 = end - start
print("se_in_10 done")
print(se_in_time_10)

# 50,000 increasing selection
start = time.process_time()
selection(nums_50)
end = time.process_time()
se_in_time_50 = end - start
print("se_in_50 done")
print(se_in_time_50)

# 1,00,000 increasing selection
start = time.process_time()
selection(nums_100)
end = time.process_time()
se_in_time_100 = end - start
print("se_in_100 done")
print(se_in_time_100)

# 10,000 increasing quick
start = time.process_time()
quick(nums_10)
end = time.process_time()
qu_in_time_10 = end - start
print("qu_in_10 done")
print(qu_in_time_10)

# 50,000 increasing quick
start = time.process_time()
quick(nums_50)
end = time.process_time()
qu_in_time_50 = end - start
print("qu_in_50 done")
print(qu_in_time_50)

# 1,00,000 increasing quick
start = time.process_time()
quick(nums_100)
end = time.process_time()
qu_in_time_100 = end - start
print("qu_in_100 done")
print(qu_in_time_100)

# Sort the array(decreasing)
nums_10.sort(reverse=True)
nums_50.sort(reverse=True)
nums_100.sort(reverse=True)

# 10,000 decreasing insertion
start = time.process_time()
insertion(nums_10)
end = time.process_time()
in_de_time_10 = end - start
print("in_de_10 done")
print(in_de_time_10)

# 50,000 decreasing insertion
start = time.process_time()
insertion(nums_50)
end = time.process_time()
in_de_time_50 = end - start
print("in_de_50 done")
print(in_de_time_50)

# 1,00,000 decreasing insertion
start = time.process_time()
insertion(nums_100)
end = time.process_time()
in_de_time_100 = end - start
print("in_de_100 done")
print(in_de_time_100)

# Sort the array(decreasing)
nums_10.sort(reverse=True)
nums_50.sort(reverse=True)
nums_100.sort(reverse=True)

# 10,000 decreasing bubble
start = time.process_time()
bubble(nums_10)
end = time.process_time()
bu_de_time_10 = end - start
print("bu_de_10 done")
print(bu_de_time_10)

# 50,000 decreasing bubble
start = time.process_time()
bubble(nums_50)
end = time.process_time()
bu_de_time_50 = end - start
print("be_de_50 done")
print(bu_de_time_50)

# 1,00,000 decreasing bubble
start = time.process_time()
bubble(nums_100)
end = time.process_time()
bu_de_time_100 = end - start
print("bu_de_100 done")
print(bu_de_time_100)

# Sort the array(decreasing)
nums_10.sort(reverse=True)
nums_50.sort(reverse=True)
nums_100.sort(reverse=True)

# 10,000 decreasing selection
start = time.process_time()
selection(nums_10)
end = time.process_time()
se_de_time_10 = end - start
print("se_de_10 done")
print(se_de_time_10)

# 50,000 increasing selection
start = time.process_time()
selection(nums_50)
end = time.process_time()
se_de_time_50 = end - start
print("se_de_50 done")
print(se_de_time_50)

# 1,00,000 increasing selection
start = time.process_time()
selection(nums_100)
end = time.process_time()
se_de_time_100 = end - start
print("se_de_100 done")
print(se_de_time_100)

# Sort the array(decreasing)
nums_10.sort(reverse=True)
nums_50.sort(reverse=True)
nums_100.sort(reverse=True)

# 10,000 decreasing quick
start = time.process_time()
quick(nums_10)
end = time.process_time()
qu_de_time_10 = end - start
print("qu_de_10 done")
print(qu_de_time_10)

# 50,000 decreasing quick
start = time.process_time()
quick(nums_50)
end = time.process_time()
qu_de_time_50 = end - start
print("qu_de_50 done")
print(qu_de_time_50)

# 1,00,000 decreasing quick
start = time.process_time()
quick(nums_100)
end = time.process_time()
qu_de_time_100 = end - start
print("qu_de_100 done")
print(qu_de_time_100)

# Plotting
x = np.array([10000, 50000, 100000])

y_in_ran = np.array([in_ran_time_10, in_ran_time_50, in_ran_time_100])
y_bu_ran = np.array([bu_ran_time_10, bu_ran_time_50, bu_ran_time_100])
y_se_ran = np.array([se_ran_time_10, se_ran_time_50, se_ran_time_100])
y_qu_ran = np.array([qu_ran_time_10, qu_ran_time_50, qu_ran_time_100])

y_in_in = np.array([in_in_time_10, in_in_time_50, in_in_time_100])
y_bu_in = np.array([bu_in_time_10, bu_in_time_50, bu_in_time_100])
y_se_in = np.array([se_in_time_10, se_in_time_50, se_in_time_100])
y_qu_in = np.array([qu_in_time_10, qu_in_time_50, qu_in_time_100])

y_in_de = np.array([in_de_time_10, in_de_time_50, in_de_time_100])
y_bu_de = np.array([bu_de_time_10, bu_de_time_50, bu_de_time_100])
y_se_de = np.array([se_de_time_10, se_de_time_50, se_de_time_100])
y_qu_de = np.array([qu_de_time_10, qu_de_time_50, qu_de_time_100])

fig, ax = plt.subplots(3)
fig.suptitle('Time Analysis')

ax[0].set_title("Random Order")
ax[0].set_xlabel("Input size")
ax[0].set_ylabel("Time in second")

ax[1].set_title("Increasing Order")
ax[1].set_xlabel("Input size")
ax[1].set_ylabel("Time in second")

ax[2].set_title("Decreasing Order")
ax[2].set_xlabel("Input size")
ax[2].set_ylabel("Time in second")

ax[0].plot(x, y_in_ran, label="Insertion")
ax[0].plot(x, y_bu_ran, label="Bubble")
ax[0].plot(x, y_se_ran, label="Selection")
ax[0].plot(x, y_qu_ran, label="Quick")
ax[0].legend(loc='upper left')

ax[1].plot(x, y_in_in, label="Insertion")
ax[1].plot(x, y_bu_in, label="Bubble")
ax[1].plot(x, y_se_in, label="Selection")
ax[1].plot(x, y_qu_in, label="Quick")
ax[1].legend(loc='upper left')

ax[2].plot(x, y_in_de, label="Insertion")
ax[2].plot(x, y_bu_de, label="Bubble")
ax[2].plot(x, y_se_de, label="Selection")
ax[2].plot(x, y_qu_de, label="Quick")
ax[2].legend(loc='upper left')

fig.tight_layout()
plt.show()
