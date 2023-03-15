# Run-Time Administration

- Run-time administration is the process of managing the memory and resources needed for the execution of a program compiled by a compiler.
- Run-time administration involves the following tasks:
  - Allocation and deallocation of memory for variables, constants, arrays, records, etc.
  - Mapping of names to memory locations and types.
  - Handling of dynamic data structures such as stacks, queues, lists, trees, etc.
  - Management of procedure calls and returns, including parameter passing and return values.
  - Handling of exceptions and errors that may occur during execution.
- Run-time administration is supported by the run-time environment, which is the structure of the target machine's registers and memory that serves to store and access the information needed for the program execution.
- The run-time environment consists of the following components:
  - Run-time support system: A package of routines that facilitates the communication between the program and the run-time environment. It takes care of memory allocation and deallocation, input/output operations, exception handling, etc.
  - Activation records: Blocks of memory that store the information related to a procedure call, such as local variables, parameters, return address, etc.
  - Activation tree: A hierarchical representation of the sequence of procedure calls and returns during the program execution. Each node in the tree corresponds to an activation record.
  - Activation stack: A linear representation of the activation tree, where the activation records are stored in a stack data structure. The top of the stack corresponds to the currently active procedure.
  - Symbol table: A data structure that stores the mapping of names to memory locations and types. It is used by the compiler and the run-time support system to access and manipulate the program data.
  - Heap: A region of memory that is used for dynamic allocation and deallocation of memory for data structures that have variable size and lifetime, such as lists, trees, etc.