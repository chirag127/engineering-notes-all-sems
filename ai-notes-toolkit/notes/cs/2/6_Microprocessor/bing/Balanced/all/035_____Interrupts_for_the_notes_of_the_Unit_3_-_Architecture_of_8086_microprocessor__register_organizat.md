# Interrupts

- Interrupts are signals that cause the CPU to suspend its current program and execute a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are triggered by external devices such as keyboards, timers, disk drives, etc. Software interrupts are triggered by instructions in the program such as INT, INTO, BOUND, etc.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR. NMI stands for non-maskable interrupt and INTR stands for maskable interrupt.
- NMI is a high-priority interrupt that cannot be disabled or ignored by the CPU. It is used for critical situations such as power failure, memory parity error, etc.
- INTR is a low-priority interrupt that can be enabled or disabled by the CPU using the EI and DI instructions. It is used for normal device communication such as keyboard input, disk I/O, etc.
- The 8086 microprocessor has 256 types of software interrupts, numbered from 0 to 255. Each interrupt has a corresponding ISR stored in a table called the interrupt vector table (IVT).
- The IVT is located at the beginning of the memory, from address 0000H to 03FFH. Each entry in the IVT is 4 bytes long and contains the segment and offset address of the ISR.
- When an interrupt occurs, the CPU performs the following steps:
  - It pushes the flags register, the code segment register, and the instruction pointer onto the stack.
  - It disables the INTR pin by clearing the IF bit in the flags register.
  - It calculates the address of the IVT entry based on the interrupt type number. For example, if the interrupt type is n, the IVT entry address is 4n.
  - It fetches the segment and offset address of the ISR from the IVT entry and loads them into the code segment register and the instruction pointer, respectively.
  - It executes the ISR until it encounters an IRET instruction, which returns the control to the interrupted program.
  - It pops the instruction pointer, the code segment register, and the flags register from the stack.
  - It resumes the execution of the interrupted program.