def bubble_sort(arr, index, loop):
    # print("loop :", loop)
    if loop == 0:
        return
    else:
        if index >= 1:
            # print("index :", index)
            if arr[index] <= arr[index - 1]:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
            bubble_sort(arr, index - 1, loop)
        else:
            bubble_sort(arr, len(arr)-1, loop - 1)


array = [5, 30, 4, 2, 1]
bubble_sort(array, 4, 4)
print(array)
