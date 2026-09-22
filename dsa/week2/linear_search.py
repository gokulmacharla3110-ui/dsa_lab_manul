# Linear Search

# Taking the number of elements
n = int(input("Enter number of elements: "))

# Taking array elements from the user
arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Taking the element to search
target = int(input("Enter element to search: "))

# Linear search
found = False

for i in range(n):
    if arr[i] == target:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")
