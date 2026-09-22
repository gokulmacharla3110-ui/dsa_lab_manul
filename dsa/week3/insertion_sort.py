# Insertion Sort

# Taking number of elements
n = int(input("Enter number of elements: "))

# Taking array elements
arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    # Move elements greater than key one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    # Insert key at correct position
    arr[j + 1] = key

print("Sorted array:", arr)
