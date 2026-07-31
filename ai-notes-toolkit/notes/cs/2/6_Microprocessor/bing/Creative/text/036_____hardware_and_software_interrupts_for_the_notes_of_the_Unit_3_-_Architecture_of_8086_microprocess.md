### Hardware and Software Interrupts

- An interrupt is a signal that causes the CPU to temporarily stop its current execution and switch to a predefined routine called an interrupt handler.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are caused by external devices that send a signal to the CPU through a dedicated pin. Software interrupts are caused by instructions in the program that generate a software interrupt request to the CPU.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR. NMI stands for non-maskable interrupt and INTR stands for maskable interrupt.
- NMI has a higher priority than INTR and cannot be disabled by the program. It is used for critical events such as power failure or parity error.
- INTR can be enabled or disabled by the program using the EI (enable interrupt) and DI (disable interrupt) instructions. It is used for normal events such as keyboard input or timer output.
- The 8086 microprocessor has 256 software interrupts, numbered from 0 to 255. Each software interrupt has a corresponding interrupt vector, which is a 4-byte pointer to the interrupt handler in memory.
- The interrupt vector table is a reserved area of memory that stores the interrupt vectors for all the interrupts. It starts from address 0000H and occupies 1024 bytes (256 x 4).
- The software interrupts can be invoked by the INT instruction, which takes an 8-bit operand that specifies the interrupt number. For example, INT 21H invokes the software interrupt 21H, which is used for DOS services.
- When an interrupt occurs, the CPU performs the following steps:
  - It saves the current flags register and the current code segment (CS) and instruction pointer (IP) on the stack.
  - It disables the INTR pin by clearing the IF (interrupt flag) bit in the flags register.
  - It calculates the address of the interrupt vector by multiplying the interrupt number by 4. For example, the address of the interrupt vector for interrupt 21H is 21H x 4 = 84H.
  - It fetches the interrupt vector from the interrupt vector table and loads it into the CS and IP registers. This causes the CPU to jump to the interrupt handler.
  - It executes the interrupt handler until it encounters an IRET (interrupt return) instruction, which restores the flags register and the CS and IP registers from the stack and resumes the interrupted program.