### Hardware and Software Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current task and execute a special subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are caused by external devices that send a signal to the microprocessor through a dedicated pin. Software interrupts are caused by instructions in the program that generate a software interrupt request to the microprocessor.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR. NMI stands for non-maskable interrupt and INTR stands for maskable interrupt.
- NMI has a higher priority than INTR and cannot be disabled by the microprocessor. It is used for critical events such as power failure or memory parity error.
- INTR can be enabled or disabled by the microprocessor using the EI (enable interrupt) and DI (disable interrupt) instructions. It is used for normal events such as keyboard input or timer output.
- The 8086 microprocessor has 256 software interrupts, numbered from 0 to 255. Each software interrupt has a corresponding interrupt vector, which is a 4-byte address that points to the ISR in memory.
- The software interrupts are invoked by the INT instruction, which takes an 8-bit operand that specifies the interrupt number. For example, INT 21H invokes the software interrupt 21H, which is used for DOS services.
- When an interrupt occurs, the microprocessor performs the following steps:
  - It saves the current flags register and the current code segment (CS) and instruction pointer (IP) registers on the stack.
  - It disables further interrupts by clearing the interrupt enable (IF) flag in the flags register.
  - It calculates the interrupt vector address by multiplying the interrupt number by 4. For example, the interrupt vector address for interrupt 21H is 21H x 4 = 84H.
  - It fetches the ISR address from the interrupt vector address and loads it into the CS and IP registers.
  - It executes the ISR until it encounters an IRET (interrupt return) instruction, which returns the control to the interrupted program.
  - It restores the flags register and the CS and IP registers from the stack.
  - It enables further interrupts by setting the IF flag in the flags register.