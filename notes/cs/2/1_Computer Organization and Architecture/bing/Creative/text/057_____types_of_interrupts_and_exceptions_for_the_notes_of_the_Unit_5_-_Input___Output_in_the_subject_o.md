### Types of Interrupts and Exceptions

- Interrupts and exceptions are events that disrupt the normal flow of execution of a program by the processor.
- Interrupts are caused by external sources, such as input/output devices, timers, or other processors.
- Exceptions are caused by internal sources, such as illegal instructions, arithmetic errors, or memory faults.
- Interrupts and exceptions can be classified into four types: normal interrupts, traps, faults, and aborts.
- Normal interrupts are asynchronous and non-maskable, meaning they can occur at any time and cannot be ignored by the processor . They are usually triggered by external devices to request service or attention from the processor . For example, a keyboard interrupt occurs when a key is pressed and the processor needs to read the input.
- Traps are synchronous and maskable, meaning they occur at a specific point in the program execution and can be disabled by the processor . They are usually caused by software instructions to invoke system calls, debugging functions, or other user-defined services . For example, a system call trap occurs when a program requests a service from the operating system, such as opening a file or printing a message.
- Faults are synchronous and maskable, meaning they occur at a specific point in the program execution and can be disabled by the processor . They are usually caused by errors or exceptional conditions that can be corrected or handled by the processor or the operating system . For example, a divide by zero fault occurs when a program attempts to divide a number by zero and the processor needs to raise an exception or terminate the program.
- Aborts are synchronous and non-maskable, meaning they occur at a specific point in the program execution and cannot be ignored by the processor . They are usually caused by severe errors or exceptional conditions that cannot be corrected or handled by the processor or the operating system . For example, a machine check abort occurs when the processor detects a hardware malfunction or a power failure and needs to halt the system.

: https://www.geeksforgeeks.org/difference-between-interrupt-and-exception/
: https://www.tutorialspoint.com/what-are-different-types-of-interrupts
: https://www.geeksforgeeks.org/interrupts-and-exceptions/