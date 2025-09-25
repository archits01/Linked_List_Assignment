# ADD: Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ADD: Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Points to top of stack (most recent)
        self.size = 0
    
    def push(self, data):
        """Add element to top of stack"""
        new_node = Node(data)
        new_node.next = self.top  # Point to previous top
        self.top = new_node       # Update top
        self.size += 1
    
    def pop(self):
        """Remove and return element from top of stack"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        data = self.top.data      # Get data from top
        self.top = self.top.next  # Move top to next element
        self.size -= 1
        return data
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None
    
    def peek(self):
        """Look at top element without removing it"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

def is_balanced(expr):
    """Check if brackets are balanced in expression"""
    # CHANGE: Use Stack class instead of list
    stack = Stack()  # instead of stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in expr:
        if char in pairs:  # Opening bracket
            stack.push(char)  # instead of stack.append(char)
        elif char in pairs.values():  # Closing bracket
            # CHANGE: Use stack methods instead of list operations
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()  # instead of not stack

def main():
    """Get input and check balance"""
    print("=== Bracket Balance Checker ===")
    print("Check if brackets (), {}, [] are balanced\n")
    
    while True:
        expr = input("Enter expression (or 'quit'): ").strip()
        
        if expr.lower() in ['quit', 'q']:
            print("Goodbye!")
            break
            
        if not expr:
            print("Empty input!\n")
            continue
            
        print("BALANCED\n" if is_balanced(expr) else "NOT BALANCED\n")

if __name__ == "__main__":
    main()
