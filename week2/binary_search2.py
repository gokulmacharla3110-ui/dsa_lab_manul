# Binary Search on an unsorted array

# Taking the number of elements
n = int(input("Enter number of elements: "))

# Taking array elements
arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Sorting the array
arr.sort()

print("Sorted array:", arr)

# Taking the element to search
target = int(input("Enter element to search: "))

# Binary search
low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at position", mid + 1)
        found = True
        break

    elif target < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1

if not found:
    print("Element not found")
