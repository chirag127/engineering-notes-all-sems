# Hardware and Software Interrupts

- An interrupt is a signal that causes the CPU to temporarily stop its current execution and switch to a different task.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are caused by external devices that send a signal to the CPU through a dedicated pin. Software interrupts are caused by instructions in the program that generate a software exception or a system call.
- The 8086 microprocessor has two pins for hardware interrupts: NMI (non-maskable interrupt) and INTR (maskable interrupt).
- NMI has a higher priority than INTR and cannot be disabled by the CPU. It is used for critical events such as power failure or parity error.
- INTR can be enabled or disabled by the CPU using the EI (enable interrupt) and DI (disable interrupt) instructions. It is used for normal events such as keyboard input or timer output.
- The 8086 microprocessor has 256 software interrupts, numbered from 0 to 255. Each software interrupt has a corresponding interrupt service routine (ISR) that is stored in a table called the interrupt vector table (IVT) at the beginning of the memory.
- The IVT contains 256 entries, each of 4 bytes, that store the segment and offset addresses of the ISR for each software interrupt. The IVT starts from address 0000:0000 and ends at 0000:03FF.
- When a hardware or software interrupt occurs, the CPU performs the following steps:
  - It pushes the flags register, the code segment register, and the instruction pointer register onto the stack.
  - It disables the INTR pin by clearing the IF (interrupt flag) bit in the flags register.
  - It calculates the address of the ISR by multiplying the interrupt number by 4 and adding it to the base address of the IVT (0000:0000).
  - It fetches the segment and offset addresses of the ISR from the calculated address and loads them into the code segment register and the instruction pointer register, respectively.
  - It executes the ISR until it encounters an IRET (interrupt return) instruction.
  - It pops the instruction pointer register, the code segment register, and the flags register from the stack.
  - It resumes the execution of the interrupted program.