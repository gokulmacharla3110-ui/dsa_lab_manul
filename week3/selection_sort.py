# Selection Sort

# Taking number of elements
n = int(input("Enter number of elements: "))

# Taking array elements
arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap minimum element with current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:", arr)
