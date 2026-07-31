### Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current execution and switch to a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are triggered by external devices such as keyboards, timers, printers, etc. that are connected to the microprocessor through dedicated pins or interrupt controllers.
- Software interrupts are triggered by special instructions in the program code, such as INT, INTO, BOUND, etc. that are used for system calls, debugging, error handling, etc.
- The 8086 microprocessor has two hardware interrupt pins: NMI (Non-Maskable Interrupt) and INTR (Maskable Interrupt).
  - NMI is a high-priority interrupt that cannot be disabled or ignored by the microprocessor. It is used for critical situations such as power failure, memory parity error, etc.
  - INTR is a low-priority interrupt that can be enabled or disabled by the microprocessor using the EI (Enable Interrupt) and DI (Disable Interrupt) instructions. It is used for normal device communication and data transfer.
- The 8086 microprocessor also has one more interrupt pin called INTA (Interrupt Acknowledge) that is used to acknowledge the receipt of an interrupt request from an external device or an interrupt controller.
- The 8086 microprocessor has 256 types of software interrupts, numbered from 0 to 255. Each interrupt type has a corresponding interrupt vector, which is a 4-byte pointer to the ISR in the memory. The interrupt vectors are stored in a table called the Interrupt Vector Table (IVT) that starts from the memory address 0x0000 and ends at 0x03FF.
- When an interrupt occurs, the microprocessor performs the following steps:
  - It pushes the current flag register and the current code segment (CS) and instruction pointer (IP) values onto the stack, to save the context of the interrupted program.
  - It calculates the address of the interrupt vector by multiplying the interrupt type number by 4. For example, the address of the interrupt vector for type 10 is 10 x 4 = 40.
  - It fetches the interrupt vector from the IVT and loads the CS and IP registers with the segment and offset values of the ISR, respectively. For example, if the interrupt vector for type 10 is 0x1234:0x5678, then CS = 0x1234 and IP = 0x5678.
  - It executes the ISR until it encounters an IRET (Interrupt Return) instruction, which pops the saved flag register, CS and IP values from the stack and resumes the interrupted program.