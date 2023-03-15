### Test and Set operation

- Test and Set Lock (TSL) is a synchronization mechanism used in concurrent processes in operating systems.
- It uses a test and set instruction to provide synchronization among the processes executing concurrently.
- The test-and-set instruction is an instruction that returns the old value of a memory location and sets the memory location value to 1 as a single atomic operation.
- This instruction ensures mutual exclusion and freedom from deadlock among the processes.