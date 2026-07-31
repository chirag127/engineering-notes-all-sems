### Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current execution and switch to a predefined subroutine called an interrupt service routine (ISR) or interrupt handler.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are caused by external devices such as keyboards, timers, printers, etc. that send a signal to the microprocessor through a dedicated pin.
- Software interrupts are caused by instructions executed by the microprocessor such as INT, INTO, BOUND, etc. that generate an interrupt request internally.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR.
  - NMI (Non-Maskable Interrupt) is a single pin non-maskable hardware interrupt that cannot be disabled. It is the highest priority interrupt in the 8086 microprocessor. It is used for emergency situations such as power failure, memory parity error, etc.  
  - INTR (Interrupt Request) is a maskable hardware interrupt that can be enabled or disabled by the software. It is used for normal peripheral devices such as keyboards, printers, etc. It has lower priority than NMI. 
- The 8086 microprocessor also has an interrupt acknowledge pin INTA that is used to acknowledge the receipt of an interrupt request from an external device. 
- The 8086 microprocessor has 256 types of interrupts, numbered from 0 to 255. Each interrupt has a corresponding ISR that is stored in a predefined memory location called the interrupt vector table (IVT).  
- The IVT starts at memory address 0x0000 and ends at 0x03FF, occupying 1 KB of memory. Each interrupt vector occupies 4 bytes of memory, consisting of a 16-bit segment address and a 16-bit offset address of the ISR. 
- The interrupt type number determines the offset of the interrupt vector in the IVT. For example, the interrupt vector for type 10H is located at offset 10H x 4 = 40H in the IVT. 
- When an interrupt occurs, the microprocessor performs the following steps:
  - It completes the execution of the current instruction and saves the flags register and the code segment register (CS) and the instruction pointer register (IP) on the stack. These registers store the address of the next instruction to be executed after returning from the ISR.
  - It disables the INTR pin to prevent further interrupts of the same or lower priority.
  - It reads the interrupt type number from the instruction (in case of software interrupt) or from the external device (in case of hardware interrupt).
  - It multiplies the interrupt type number by 4 and adds it to the base address of the IVT (0x0000) to obtain the address of the interrupt vector.
  - It reads the segment address and the offset address of the ISR from the interrupt vector and loads them into the CS and IP registers, respectively. This causes the microprocessor to jump to the ISR.
  - It executes the ISR until it encounters an IRET (interrupt return) instruction, which restores the flags register and the CS and IP registers from the stack and resumes the execution of the interrupted program.