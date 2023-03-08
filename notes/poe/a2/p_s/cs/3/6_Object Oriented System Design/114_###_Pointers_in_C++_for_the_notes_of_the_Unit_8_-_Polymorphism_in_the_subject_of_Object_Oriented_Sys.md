 Here are the points on ### Pointers in C++ for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design:

1. A pointer is a variable that stores the address of another variable. It is a memory address that points to the location of another value stored in memory.
2. To declare a pointer, precede the name of the variable with an asterisk (*). For example, int* ptr; declares ptr as a pointer to an int.
3. To access the value that a pointer points to, use the dereference operator (*). For example, if ptr points to an integer, *ptr accesses the integer value.
4. Pointers allow passing of arguments by reference, enabling efficient processing. They are also essential for implementing dynamic data structures like linked lists, trees, etc.
5. Pointers have many applications like -
    - They are used to dynamically allocate memory in C++ using new and delete operators.
    - Used in call-by-reference method of function argument passing. This method is efficient when large structures are passed as arguments to functions.
    - Used to create and manipulate various data structures like linked lists, trees, graphs, etc.
    - Used in the implementation of polymorphism in C++. The virtual function table is created using pointers.
    - Used in improving performance by identifying and passing addresses instead of the entire value of variables.
6. However, pointers can be tricky to use and bugs due to invalid pointers are difficult to debug. Proper usage and management of pointers is important to avoid such issues.

[Detailed diagrams and code snippets can be added here to supplement the points and make the notes more comprehensive.]