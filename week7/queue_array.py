class ArrayQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(item, "inserted")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
        else:
            item = self.queue[self.front]
            self.front += 1

            if self.front > self.rear:
                self.front = self.rear = -1

            print(item, "deleted")

    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front element =", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Queue:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# -------- Main Program --------
size = int(input("Enter Queue Size: "))
q = ArrayQueue(size)

while True:
    print("\n--- ARRAY QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        q.enqueue(item)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
