def count(n):
    if n == 0:
        print("launch")
        return
    print(n)
    count(n-1)


n= int(input("Enter countdown number: "))
count(n)
