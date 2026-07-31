 Here is the formal content in markdown format without any feeling or friendliness for the given topic:

### Abstract Data Types : Abstract data types and ADT interface in Python Programming.

1. Abstract Data Type (ADT) is a type (or class) for objects whose behavior is defined by a set of value and a set of operations. The definition of ADT only mentions what operations are to be performed but not how these operations will be implemented.
2. ADT separates the interface and implementation. The interface describes the behavior of the data type in terms of operations, while the implementation describes the data structure and algorithms used to support the operations.
3. Some examples of ADTs are:
- Stack: push, pop, peek
- Queue: enqueue, dequeue
- List: insert, append, remove
- Tree: insert, delete, search

4. In Python, we can implement ADTs using class. The class describes the structure and interface of the ADT, and the methods of the class implement the operations. For example:
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

5. The program defines the Stack ADT by specifying the structure (as a list) and the operations on the stack (push, pop, peek, is_empty). The actual implementation of these operations is hidden from the user of the ADT.