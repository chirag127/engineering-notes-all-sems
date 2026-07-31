### Interrupts

- Interrupts are signals that cause the microprocessor to suspend its current operation and execute a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are caused by external devices that send a signal to the microprocessor through a dedicated pin. Software interrupts are caused by instructions executed by the microprocessor.
- The 8086 microprocessor has two hardware interrupt pins: NMI (Non-Maskable Interrupt) and INTR (Interrupt Request).
  - NMI is a high-priority interrupt that cannot be disabled or ignored by the microprocessor. It is used for critical events that require immediate attention, such as power failure or parity error.
  - INTR is a low-priority interrupt that can be enabled or disabled by the microprocessor using the interrupt enable (IF) flag in the flags register. It is used for normal events that can be handled at a convenient time, such as keyboard input or disk access.
- The 8086 microprocessor has 256 types of software interrupts, numbered from 0 to 255. Each type of interrupt has a corresponding ISR that is stored in a table called the Interrupt Vector Table (IVT).
  - The IVT is located in the memory address range from 0x0000 to 0x03FF. Each entry in the IVT is 4 bytes long and contains the segment and offset address of the ISR for that interrupt type.
  - The interrupt type number is multiplied by 4 to get the offset of the IVT entry for that interrupt. For example, the IVT entry for interrupt type 10h is at offset 40h in the IVT.
  - When a software interrupt is executed, the microprocessor pushes the flags register, the code segment register, and the instruction pointer register onto the stack, and then jumps to the ISR address stored in the IVT entry for that interrupt type.
  - When the ISR is completed, the microprocessor executes an IRET (Interrupt Return) instruction, which pops the instruction pointer, the code segment, and the flags register from the stack, and resumes the interrupted program.
- Some of the software interrupts are predefined by Intel and have specific functions. For example, interrupt type 21h is used for DOS services, such as file operations, input/output operations, memory allocation, etc.