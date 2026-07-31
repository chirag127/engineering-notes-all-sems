### Run-Time Administration

Run-Time Administration is an essential part of Compiler Design. It is responsible for managing the execution of the program while it is running. In this section, we will cover the concepts related to Run-Time Administration for Symbol Tables in Compiler Design.

1. **Symbol Tables**:

Symbol tables are the data structures used to store the information about the symbols used in the program. It contains the name, type, and value of the symbol. The symbol table is used by the compiler during the compilation phase to check the validity of the program.

2. **Run-Time Stack**:

The Run-Time Stack is a data structure used by the compiler during the execution phase of the program. It stores the information about the function calls, local variables, and return addresses. The stack is used to keep track of the execution of the program.

3. **Activation Record**:

An activation record is a data structure used to store the information about a function call. It contains the return address, the value of the parameters, and the local variables used in the function. The activation record is pushed onto the Run-Time Stack whenever a function is called.

4. **Parameter Passing**:

Parameter passing is the process of passing the parameters to a function. There are two types of parameter passing: 

- **Pass by Value**: In this type of parameter passing, the values of the parameters are passed to the function. Any changes made to the parameters inside the function do not affect the original values.

- **Pass by Reference**: In this type of parameter passing, the reference to the parameters is passed to the function. Any changes made to the parameters inside the function will affect the original values.

5. **Memory Management**:

Memory management is the process of allocating and deallocating memory for the program. The memory is allocated during the execution phase of the program. The Run-Time Stack is used to store the memory used by the program. The memory is deallocated when the program terminates.

6. **Exception Handling**:

Exception handling is the process of handling the errors that occur during the execution of the program. The exceptions can be handled by using try-catch blocks. The exceptions can be caught and handled by the program.

In conclusion, Run-Time Administration is an essential part of Compiler Design. It is responsible for managing the execution of the program while it is running. The concepts related to Symbol Tables, Run-Time Stack, Activation Record, Parameter Passing, Memory Management, and Exception Handling are essential to understand the Run-Time Administration.