# Hardware and Software Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current task and execute a special subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.

## Hardware Interrupts

- Hardware interrupts are caused by external devices that are connected to the microprocessor through dedicated pins.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR.
- NMI stands for non-maskable interrupt and it has the highest priority among all interrupts. It cannot be disabled or ignored by the microprocessor. It is usually used for critical events such as power failure or memory parity error.
- INTR stands for interrupt request and it is a maskable interrupt that can be enabled or disabled by the microprocessor using the interrupt enable (IF) flag in the flags register. It has a lower priority than NMI and it is used for normal events such as keyboard input or disk access.
- When a hardware interrupt occurs, the microprocessor performs the following steps:
  - It completes the current instruction and saves the flags register and the instruction pointer (IP) on the stack.
  - It clears the IF flag to disable further interrupts.
  - It acknowledges the interrupt by sending a signal to the interrupt controller, which is a separate chip that manages the interrupt requests from multiple devices.
  - It obtains the interrupt vector, which is a 16-bit address that points to the ISR, from the interrupt controller or from a fixed location in memory depending on the type of interrupt.
  - It loads the interrupt vector into the IP and jumps to the ISR.
  - It executes the ISR until it encounters an interrupt return (IRET) instruction, which restores the flags register and the IP from the stack and resumes the interrupted program.

## Software Interrupts

- Software interrupts are caused by program instructions that are executed by the microprocessor.
- The 8086 microprocessor has 256 software interrupts, numbered from 0 to 255, that can be invoked by using the interrupt (INT) instruction followed by an 8-bit operand that specifies the interrupt number.
- Each software interrupt has a corresponding interrupt vector that is stored in a table called the interrupt vector table (IVT), which occupies the first 1024 bytes of memory from address 0000H to 03FFH.
- The interrupt vector for a software interrupt n is stored at the address 4n (low byte) and 4n+1 (high byte) in the IVT.
- When a software interrupt occurs, the microprocessor performs the following steps:
  - It completes the current instruction and saves the flags register and the IP on the stack.
  - It clears the IF flag to disable further interrupts.
  - It obtains the interrupt vector from the IVT using the interrupt number as an index.
  - It loads the interrupt vector into the IP and jumps to the ISR.
  - It executes the ISR until it encounters an IRET instruction, which restores the flags register and the IP from the stack and resumes the interrupted program.
- Software interrupts are used for various purposes such as system calls, debugging, error handling, and user-defined functions.