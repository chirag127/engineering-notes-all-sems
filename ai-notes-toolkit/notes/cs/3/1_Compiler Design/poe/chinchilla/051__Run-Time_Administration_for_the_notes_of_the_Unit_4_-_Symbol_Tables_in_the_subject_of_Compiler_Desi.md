### Run-Time Administration

Run-time administration involves the management of program execution during the runtime of a program. This is accomplished through the use of symbol tables, which are data structures used to maintain information about program variables and their values. In this section, we will discuss the various aspects of run-time administration and how symbol tables are used to facilitate it.

#### Symbol Tables

Symbol tables are data structures used to store information about program variables, such as their names, types, and memory locations. Symbol tables are typically implemented as hash tables, which provide efficient lookup and insertion of key-value pairs.

Symbol tables are used extensively during program execution to access and manipulate program variables. When a variable is declared in a program, it is added to the symbol table along with its corresponding data. During program execution, the symbol table is used to look up the memory location of the variable so that it can be accessed or modified.

#### Scope

Scope refers to the visibility of program variables within the program. A variable's scope determines where it can be accessed and modified. There are two main types of scope: global scope and local scope.

Global scope variables are visible throughout the entire program and can be accessed and modified from anywhere in the program. Local scope variables, on the other hand, are only visible within a specific block of code, such as a function or loop. Local scope variables cannot be accessed or modified outside of their block of code.

Symbol tables are used to manage scope during program execution. When a new block of code is entered, a new symbol table is created to store information about the variables in that block. When the block is exited, the symbol table is destroyed and any variables stored in it are no longer accessible.

#### Memory Management

Memory management is an important aspect of run-time administration. When a program is executed, it requires memory to store program variables and data. Symbol tables are used to manage memory during program execution.

When a variable is declared in a program, its memory location is obtained from the symbol table. The symbol table keeps track of which memory locations are available and which are in use. When a variable is no longer needed, its memory location is released back to the symbol table for reuse.

#### Exception Handling

Exception handling is another important aspect of run-time administration. Exceptions are errors or unexpected events that occur during program execution. Symbol tables are used to manage exception handling by storing information about the state of the program at the time the exception occurred.

When an exception occurs, the symbol table is used to determine the location and state of the program at the time of the exception. This information can be used to diagnose and fix the problem that caused the exception.

#### Conclusion

In summary, run-time administration is the management of program execution during runtime. Symbol tables are data structures used to store information about program variables and facilitate run-time administration. Symbol tables are used to manage scope, memory, and exception handling during program execution. Understanding run-time administration and symbol tables is crucial for designing and implementing efficient and error-free programs.