# Bubble Sort

# Taking number of elements
n = int(input("Enter number of elements: "))

# Taking array elements
arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            # Swap elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    # Stop if array is already sorted
    if not swapped:
        break

print("Sorted array:", arr)
