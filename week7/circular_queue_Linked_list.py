class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new = Node(item)

        if self.front is None:
            self.front = self.rear = new
            self.rear.next = self.front
        else:
            self.rear.next = new
            self.rear = new
            self.rear.next = self.front

        print(item, "inserted")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        item = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print(item, "deleted")

    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Front element =", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front
        print("Circular Queue:", end=" ")

        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:
                break
        print()


# -------- MAIN --------
q = CircularLinkedQueue()

while True:
    print("\n--- CIRCULAR QUEUE (LINKED LIST) ---")
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
