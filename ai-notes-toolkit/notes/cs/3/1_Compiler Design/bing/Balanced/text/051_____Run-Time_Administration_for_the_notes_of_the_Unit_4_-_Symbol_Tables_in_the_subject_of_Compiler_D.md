### Run-Time Administration for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design

- Run-time administration is the process of managing the memory and other resources needed by a program during its execution.
- Run-time administration involves the following tasks:
  - Allocating and de-allocating memory for variables, arrays, records, objects, etc.
  - Maintaining information about the scope and lifetime of variables and procedures.
  - Implementing parameter passing mechanisms and return values for procedures.
  - Handling dynamic memory allocation and garbage collection for heap-allocated objects.
  - Supporting run-time checks and exceptions for errors such as array bounds violation, division by zero, etc.
- Run-time administration is closely related to the design of the symbol table, which is a data structure that stores information about the names and attributes of the entities in a program, such as variables, constants, types, procedures, etc.
- The symbol table is used by the compiler to perform semantic analysis, type checking, code generation, and optimization.
- The symbol table is also used by the run-time system to access and manipulate the entities in the program during execution.
- The symbol table can be organized in different ways, such as linear lists, hash tables, trees, etc.
- The symbol table can also be divided into different levels or scopes, such as global, local, nested, etc.
- The symbol table can also be augmented with additional information, such as offsets, addresses, registers, etc., to facilitate code generation and run-time administration.
- The run-time system can use different techniques to implement run-time administration, such as static allocation, stack allocation, heap allocation, etc.
- Static allocation is the technique of allocating memory for variables and procedures at compile time, based on their size and scope. Static allocation is simple and efficient, but does not support dynamic features such as recursion, dynamic arrays, etc.
- Stack allocation is the technique of allocating memory for variables and procedures at run time, using a data structure called the stack. The stack grows and shrinks as procedures are called and returned, and variables are created and destroyed. Stack allocation supports recursion, local variables, parameter passing, etc., but has limited size and requires stack discipline.
- Heap allocation is the technique of allocating memory for variables and procedures at run time, using a data structure called the heap. The heap is a pool of free memory that can be allocated and de-allocated as needed. Heap allocation supports dynamic features such as dynamic arrays, objects, closures, etc., but requires more memory management and may cause fragmentation and garbage collection issues.