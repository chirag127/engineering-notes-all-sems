### Types of Interrupts and Exceptions

- Interrupts and exceptions are events that disrupt the normal flow of execution of a program by the processor.
- Interrupts are caused by external sources, such as input/output devices, timers, or other processors.
- Exceptions are caused by internal sources, such as illegal instructions, arithmetic errors, or memory faults.
- Interrupts and exceptions can be classified into four types: interrupt, trap, fault, and abort.
- Interrupt: A type of exception that is triggered by an external signal or a software instruction. It is usually used for handling asynchronous events, such as keyboard input, disk access, or inter-processor communication  .
- Trap: A type of exception that is triggered by an intentional instruction, such as a system call, a breakpoint, or a debug operation. It is usually used for switching from user mode to kernel mode, or for invoking privileged services  .
- Fault: A type of exception that is triggered by an error condition, such as a division by zero, an invalid memory access, or a page fault. It is usually recoverable, meaning that the processor can resume the execution of the faulting instruction after correcting the error or handling the exception  .
- Abort: A type of exception that is triggered by a severe error condition, such as a machine check, a parity error, or a protection violation. It is usually unrecoverable, meaning that the processor cannot resume the execution of the aborting instruction or the program  .