# WEEK 10 - HASHING
# Separate Chaining, Linear Probing and Quadratic Probing

# Function for Separate Chaining
def separate_chaining():
    size = int(input("Enter hash table size: "))

    table = [[] for _ in range(size)]

    n = int(input("Enter number of elements: "))

    for i in range(n):
        key = int(input("Enter key: "))
        index = key % size
        table[index].append(key)

    print("\nSeparate Chaining:")
    for i in range(size):
        print(i, ":", table[i])


# Function for Linear Probing
def linear_probing():
    size = int(input("Enter hash table size: "))

    table = [-1] * size

    n = int(input("Enter number of elements: "))

    for i in range(n):
        key = int(input("Enter key: "))

        index = key % size
        start = index

        while table[index] != -1:
            index = (index + 1) % size

            if index == start:
                print("Hash table is full!")
                break

        else:
            table[index] = key

    print("\nLinear Probing:")
    for i in range(size):
        print(i, ":", table[i])


# Function for Quadratic Probing
def quadratic_probing():
    size = int(input("Enter hash table size: "))

    table = [-1] * size

    n = int(input("Enter number of elements: "))

    for i in range(n):
        key = int(input("Enter key: "))

        hash_index = key % size
        j = 0

        while j < size:
            index = (hash_index + j * j) % size

            if table[index] == -1:
                table[index] = key
                break

            j = j + 1

        if j == size:
            print("Hash table is full!")

    print("\nQuadratic Probing:")
    for i in range(size):
        print(i, ":", table[i])


# Main program
while True:

    print("\n========== HASHING ==========")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        separate_chaining()

    elif choice == 2:
        linear_probing()

    elif choice == 3:
        quadratic_probing()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
        
        
