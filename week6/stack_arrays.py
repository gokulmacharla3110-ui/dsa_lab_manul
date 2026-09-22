class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(data, "pushed")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Popped:", self.stack.pop())

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", end=" ")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i], end=" ")
            print()


s = StackArray()

while True:
    print("\n--- STACK USING ARRAY ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
