### Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current operation and transfer the control to a special routine, called an interrupt service routine (ISR), that handles the event.
- The ISR performs the required tasks and then returns the control to the point of interruption.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.

#### Hardware Interrupts

- Hardware interrupt is caused by any peripheral device by sending a signal through a specified pin to the microprocessor.
- The 8086 has two hardware interrupt pins, i.e. NMI and INTR.
- NMI is a non-maskable interrupt and INTR is a maskable interrupt having lower priority.
- NMI is a single pin non-maskable hardware interrupt that cannot be disabled. It is the highest priority interrupt in the 8086 microprocessor .
- INTR is a maskable interrupt that can be enabled or disabled by using the instructions STI (set interrupt flag) and CLI (clear interrupt flag).
- INTR is used for requesting the microprocessor to execute a subroutine. The microprocessor sends an interrupt acknowledge signal (INTA) to the requesting device and then executes the ISR.
- The ISR address for NMI is fixed at 0000:0008H and for INTR is given by the interrupt vector table (IVT).

#### Software Interrupts

- Software interrupt is caused by executing an instruction that generates an interrupt request.
- The 8086 microprocessor has 256 types of software interrupts, numbered from 0 to 255.
- Each software interrupt has a type number, which is used to access the ISR address from the IVT.
- The IVT starts at memory address 0000:0000H and can go as high as 0000:03FFH, for a maximum number of 256 ISRs (ranging from interrupt 0 to 255).
- The IVT contains 256 four-byte pointers, each pointing to the start of an ISR.
- The software interrupt instruction is INT n, where n is the type number of the interrupt.
- The INT n instruction pushes the flags, CS and IP registers onto the stack and then jumps to the ISR address given by the IVT.
- The ISR can return the control to the main program by using the IRET instruction, which pops the IP, CS and flags registers from the stack.