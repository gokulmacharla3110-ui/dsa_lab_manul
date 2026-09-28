class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(item, "inserted")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

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
        print("Queue:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# -------- Main Program --------
q = LinkedQueue()

while True:
    print("\n--- LINKED LIST QUEUE MENU ---")
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
        
