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
        if a1[i]['v/w'] >= a2[j]['v/w']:
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
    arr


items = []
no_item = int(input("How many items you have : "))

for i in range(no_item):
    item = {}
    print(f"Item No. {i+1} :")
    weight = int(input("Enter Weight : "))
    value = int(input("Enter Value : "))
    v_w = value/weight
    item['weight'] = weight
    item['value'] = value
    item['v/w'] = v_w
    item['name'] = f"Item{i+1}"
    items.append(item)

items.sort(key=lambda x: (x['value']/x['weight']), reverse=True)
# sorting the knapsack
# merge(0, len(items)-1, items)

print(items)
taken_item = []
capacity = int(input("Enter Capacity of Knapsack :"))
profit = 0
for item in items:
    if capacity > 0:
        i = {}
        if capacity > item['weight']:
            capacity = capacity - item['weight']
            profit = profit + item['value']
            i['value'] = item['value']
            i['weight'] = item['weight']
            i['name'] = item['name']
            taken_item.append(i)
        else:
            profit = profit + item['v/w']*capacity
            i['value'] = item['v/w']*capacity
            i['weight'] = capacity
            i['name'] = item['name']
            taken_item.append(i)
            capacity = 0
    else:
        break

if capacity > 0:
    print("Remaining capacity of Knapsack : ", capacity)
print("Total Profit :", profit)
print("Items part of Knapsack : ", taken_item)
