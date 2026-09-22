def main():
    print("rollno : cse25126\nname : M.Gokul krishna\n")
    n = int(input("Enter size of array: "))
    arr = []
    for i in range(n):
        arr.append(int(input(f"enter {i+1} element: ")))
    quick_sort(arr, 0, n-1)
    print(arr)


def quick_sort(a, low, high):
    if low < high:
        pivot = a[low]      # store pivot VALUE, not index
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while a[i] < pivot:
                i += 1
            j -= 1
            while a[j] > pivot:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]

        quick_sort(a, low, j)      # left part (includes j)
        quick_sort(a, j + 1, high) # right part


if __name__ == '__main__':
    main()
