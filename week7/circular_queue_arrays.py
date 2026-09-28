class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = item
        print(item, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return

        item = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(item, "deleted")

    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front element =", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# -------- MAIN --------
size = int(input("Enter Queue Size: "))
q = CircularQueue(size)

while True:
    print("\n--- CIRCULAR QUEUE (ARRAY) ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter element: "))
        q.enqueue(x)

    elif ch == 2:
        q.dequeue()

    elif ch == 3:
        q.peek()

    elif ch == 4:
        q.display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
