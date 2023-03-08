### Interrupts

- Interrupts are a mechanism to temporarily halt the normal execution of a program and transfer the control to a special routine that handles an event or a situation.
- Interrupts can be caused by external devices, such as keyboards, printers, timers, etc., or by internal events, such as division by zero, overflow, etc.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.

#### Hardware Interrupts

- Hardware interrupts are those interrupts that are caused by any peripheral device by sending a signal through a specified pin to the microprocessor.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR.
- NMI (Non-Maskable Interrupt) is a single pin non-maskable hardware interrupt that cannot be disabled. It is the highest priority interrupt in the 8086 microprocessor. It is usually used for power failure or emergency stop situations.
- INTR (Interrupt Request) is a maskable hardware interrupt that can be enabled or disabled by using the EI (Enable Interrupt) and DI (Disable Interrupt) instructions. It is a lower priority interrupt than NMI. It is used for normal device requests, such as keyboard input, disk access, etc.
- When a hardware interrupt occurs, the microprocessor completes the current instruction and saves the flags register and the CS:IP registers on the stack. Then, it acknowledges the interrupt by sending a signal through the INTA (Interrupt Acknowledge) pin. The interrupting device then sends an 8-bit vector number to the microprocessor, which is used to locate the address of the interrupt service routine (ISR) in the interrupt vector table (IVT). The IVT is a 256-entry table that starts from the memory location 0000:0000H and contains the CS:IP addresses of the ISRs for each interrupt vector. The microprocessor then jumps to the ISR and executes it. After the ISR is completed, the microprocessor returns to the interrupted program by using the IRET (Interrupt Return) instruction, which pops the CS:IP and the flags register from the stack.

#### Software Interrupts

- Software interrupts are those interrupts that are caused by executing an instruction in the program, such as INT, INTO, BOUND, etc.
- The 8086 microprocessor supports 256 software interrupts, from INT 00H to INT FFH. Each software interrupt has a corresponding vector number, which is used to locate the ISR in the IVT, similar to hardware interrupts.
- Some of the software interrupts are predefined and reserved for specific functions, such as BIOS routines, DOS services, etc. For example, INT 10H is used for video services, INT 13H is used for disk services, INT 21H is used for DOS functions, etc. These interrupts are also called BIOS interrupts or DOS interrupts.
- The user can also define and use software interrupts for their own purposes, such as subroutines, exception handling, etc. These interrupts are also called user-defined interrupts or application interrupts.
- When a software interrupt occurs, the microprocessor performs the same steps as a hardware interrupt, except that it does not acknowledge the interrupt through the INTA pin. Instead, it directly uses the vector number from the instruction to locate the ISR in the IVT and jumps to it. After the ISR is completed, the microprocessor returns to the interrupted program by using the IRET instruction.

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of the flags in the flags register, use the acronym OF DITS ZA P C, where each letter stands for a flag: Overflow, Direction, Interrupt, Trap, Sign, Zero, Auxiliary Carry, Parity, Carry.
- To remember the names and functions of the 16-bit general purpose registers, use the acronym AX BX CX DX, where each letter stands for a register: Accumulator, Base, Count, Data. The functions are:

  - Accumulator: used for arithmetic, logic, data transfer, and I/O operations.
  - Base: used as a base pointer for memory access in the stack segment.
  - Count: used as a counter or an index for string and loop operations.
  - Data: used for arithmetic, logic, and data transfer operations.

- To remember the names and functions of the 16-bit segment registers, use the acronym CS DS SS ES, where each letter stands for a register: Code, Data, Stack, Extra. The functions are:

  - Code: used to store the segment address of the code segment, where the program instructions are stored.
  - Data: used to store the segment address of the data segment, where the program data are stored.
  - Stack: used to store the segment address of the stack segment, where the program stack is stored.
  - Extra: used to store the segment address of an extra segment, which can be used for additional data storage.

- To remember the names and functions of the 16-bit pointer and index registers, use the acronym SP BP SI DI, where each letter stands for a register: Stack Pointer, Base Pointer, Source Index, Destination Index. The functions are:

  - Stack Pointer: used to store the offset address of the top of the stack in the stack segment.
  - Base Pointer: used to store the offset address of the base of the stack frame in the stack segment.
  - Source Index: used to store the offset address of the source operand in string operations.
  - Destination Index: used to store the offset address of the destination operand in string operations.

- To remember the names and functions of the 8-bit registers, use the acronym AH AL BH BL CH CL DH DL, where each letter stands for a register: High, Low. The functions are:

  - High: used to store the high-order 8 bits of the corresponding 16-bit register.
  - Low: used to store the low-order 8 bits of the corresponding 16-bit register.