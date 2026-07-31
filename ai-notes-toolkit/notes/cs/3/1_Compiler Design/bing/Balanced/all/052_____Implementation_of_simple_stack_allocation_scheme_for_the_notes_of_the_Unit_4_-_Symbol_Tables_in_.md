# Implementation of simple stack allocation scheme

- Stack allocation scheme is the simplest run-time storage management technique   .
- The storage is organized as a stack, and activation records are pushed and popped as the activation of procedures begin and end, respectively  .
- Activation records contain information about the state of a procedure, such as its parameters, local variables, return address, etc.
- Stack allocation allows recursive procedures, since each recursive call creates a new activation record on the stack .
- Stack allocation also supports dynamic scoping, where the binding of a variable depends on the most recent declaration in the current or enclosing procedure.
- Stack allocation has some limitations, such as :
  - It requires storage to be freed in the reverse order of allocation, which may not match the lifetime of some variables.
  - It leads to variable-size stack frames, which require both stack and frame pointers to be managed.
  - It does not support procedures as first-class values, since the activation record of a procedure may be deallocated when the procedure returns.
- The implementation of stack allocation scheme involves the following steps:
  - Allocation of variable-length data, such as arrays or strings, on the heap or in a separate stack.
  - Generation of calling sequences, which are code segments that handle the creation and deletion of activation records, as well as the passing of parameters and return values.
  - Management of stack and frame pointers, which are registers that point to the top of the stack and the current activation record, respectively.
  - Access of non-local variables, which are variables declared in an enclosing procedure, by using static links or display registers.