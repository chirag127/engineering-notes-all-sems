
### Implementation of Simple Stack Allocation Scheme for the Notes of Unit 4 - Symbol Tables in Compiler Design

* Stack allocation is a process in which the compiler allocates memory to a program's variables. It is a form of memory management that is often used in compilers to allocate memory to variables within a program. 
* In stack allocation, memory is allocated in a stack-like structure, with the most recently allocated memory being the first to be deallocated. This is done by pushing variables onto the stack and popping them off when they are no longer needed. 
* Stack allocation is an efficient way of managing memory, as it does not require the compiler to search through the entire memory to find a suitable location for a variable. 
* It also allows for quick access to the most recently allocated variables, as they are always at the top of the stack. 
* The main advantage of stack allocation is that it is fast and efficient. It is also relatively easy to implement, as the compiler simply needs to keep track of the top of the stack and the size of the stack. 
* However, one of the main disadvantages of stack allocation is that it can lead to memory fragmentation. This occurs when the compiler is unable to find a large enough block of memory for a variable, and so it must allocate smaller chunks of memory. This can lead to memory being wasted as the compiler is unable to use the smaller chunks of memory for anything else. 
* Another disadvantage of stack allocation is that it is not suitable for programs with large numbers of variables. This is because the compiler must keep track of all the variables on the stack, which can become a complex task. 
* Stack allocation is often used in compilers for symbol tables. Symbol tables are used to store information about variables, functions and other symbols used in a program. 
* In a symbol table, each symbol is assigned a unique address. The compiler can then use this address to quickly look up information about the symbol, such as its type, size and scope. 
* Stack allocation is often used to allocate memory for symbol tables, as it is an efficient way of managing memory. The compiler can simply push the symbol onto the stack and pop it off when it is no longer needed. 
* Stack allocation can also be used to allocate memory for other data structures, such as linked lists and trees. By pushing and popping elements onto the stack, the compiler can quickly allocate memory for these data structures. 
* In summary, stack allocation is an efficient way of managing memory in compilers. It is fast and easy to implement, but can lead to memory fragmentation and is not suitable for programs with large numbers of variables. It is often used for symbol tables and other data structures.