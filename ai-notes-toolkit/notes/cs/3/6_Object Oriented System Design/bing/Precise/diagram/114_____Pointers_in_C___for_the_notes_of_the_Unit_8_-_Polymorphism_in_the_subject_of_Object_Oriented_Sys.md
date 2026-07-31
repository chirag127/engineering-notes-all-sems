### Pointers in C++

Pointers are a powerful feature of the C++ programming language that allows you to directly manipulate memory addresses. They are used to store the memory addresses of variables, which can be used to indirectly access the value stored in that memory location. Here are some key points to remember about pointers in C++:

1. Pointers are declared using the `*` symbol. For example, `int *ptr;` declares a pointer to an integer variable.
2. The `&` operator is used to obtain the memory address of a variable. For example, `ptr = &x;` assigns the memory address of the variable `x` to the pointer `ptr`.
3. The `*` operator is used to dereference a pointer, which means to access the value stored in the memory location pointed to by the pointer. For example, `*ptr = 10;` assigns the value `10` to the memory location pointed to by `ptr`.
4. Pointers can be used to pass variables by reference to functions. This allows the function to modify the value of the variable passed to it.
5. Pointers can be used to dynamically allocate memory using the `new` and `delete` operators. This allows you to create and destroy objects at runtime.
6. Pointers can be used to create and manipulate arrays. For example, you can use pointer arithmetic to iterate through the elements of an array.
7. Pointers can be used to implement polymorphism in C++. By creating a pointer to a base class, you can assign it to an object of a derived class, allowing you to call virtual functions defined in the base class.
