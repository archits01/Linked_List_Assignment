# ADD: Node class (new)
class Node:
    def __init__(self, message):
        self.message = message
        self.next = None

class MessagingQueue:
    def __init__(self):
        # CHANGE: Replace list with head/tail pointers
        self.head = None  # instead of self.messages = []
        self.tail = None

    def add(self, message):
        # CHANGE: Create node and link it
        new_node = Node(message)  # instead of self.messages.append(message)
        
        if self.tail is None:  # empty queue
            self.head = self.tail = new_node
        else:  # link to existing chain
            self.tail.next = new_node
            self.tail = new_node
            
        print("Added:", message)

    def deliver(self):
        # CHANGE: Check head instead of list
        if self.head is None:  # instead of if not self.messages:
            print("Queue is empty!")
            return None
            
        # CHANGE: Get message from head node
        msg = self.head.message  # instead of self.messages.pop(0)
        self.head = self.head.next
        
        # Update tail if queue becomes empty
        if self.head is None:
            self.tail = None
            
        print("Delivered:", msg)
        return msg

    def show(self):
        # CHANGE: Check head and traverse nodes
        if self.head is None:  # instead of if not self.messages:
            print("Queue is empty!")
        else:
            # Build list by traversing nodes
            messages = []
            current = self.head
            while current:
                messages.append(current.message)
                current = current.next
            print("Queue:", messages)  # same output format


# UNCHANGED: Main function stays exactly the same
def main():
    q = MessagingQueue()
    print("Commands: add, deliver, show, quit")

    while True:
        cmd = input("Enter command: ").lower()

        if cmd == "quit":
            print("Bye!")
            break
        elif cmd == "add":
            msg = input("Enter message: ")
            q.add(msg)
        elif cmd == "deliver":
            q.deliver()
        elif cmd == "show":
            q.show()
        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()
