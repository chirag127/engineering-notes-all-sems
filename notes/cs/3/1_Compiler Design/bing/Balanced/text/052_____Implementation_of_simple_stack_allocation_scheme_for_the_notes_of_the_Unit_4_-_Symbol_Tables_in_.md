### Implementation of simple stack allocation scheme

- Stack allocation is a runtime storage management technique for the compiler  whereby activation records are pushed and popped onto the stack as activations begin and end by use of predefined routines in the compiler.
- Activation records are data structures that contain information about the execution of a procedure, such as parameters, local variables, return address, etc.
- Stack allocation allows recursive procedures, since each activation of a procedure has its own activation record on the stack.
- Stack allocation is simple and efficient, but it has some limitations, such as:
  - It requires that the lifetime of a procedure activation is nested within the lifetime of its caller, which may not be the case for some languages that allow non-local references or dynamic scoping.
  - It does not support dynamic allocation of variable-length data, such as arrays or strings, within activation records, since the size of the activation record must be known at compile time.
  - It leads to variable-size stack frames, which require both stack and frame pointers to be managed, adding some overhead to the execution.
- To implement stack allocation, the compiler needs to generate code for the following tasks:
  - Allocate space for the activation record on the stack when a procedure is called, by decrementing the stack pointer by the size of the activation record.
  - Store the parameters, return address, and old frame pointer in the activation record, and set the new frame pointer to point to the top of the stack.
  - Access the local variables and parameters within the activation record, by using offsets from the frame pointer.
  - Deallocate space for the activation record on the stack when a procedure returns, by restoring the old frame pointer and incrementing the stack pointer by the size of the activation record.
  - Retrieve the return address and the return value from the activation record, and jump to the caller.