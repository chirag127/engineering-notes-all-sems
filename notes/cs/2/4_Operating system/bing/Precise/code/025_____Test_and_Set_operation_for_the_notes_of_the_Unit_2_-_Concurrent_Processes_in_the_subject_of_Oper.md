### Test and Set operation for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- Test and Set Lock (TSL) is a synchronization mechanism. It uses a test and set instruction to provide the synchronization among the processes executing concurrently.
- Test-and-Set Instruction is an instruction that returns the old value of a memory location and sets the memory location value to 1 as a single atomic operation.
- Maurice Herlihy(1991) proved that test-and-set (1-bit comparand) has a finite consensus number and can solve the wait-free consensus problem for at-most two concurrent processes.
- Concurrent processing is a computing model in which multiple processors execute instructions simultaneously for better performance.
- Concurrent processes come into conflict when they are competing for use of the same resource for example: I/O devices, memory, processor time, clock.
- 3 control problems must be faced: 1) The need for mutual exclusion 2) deadlock 3) starvation.