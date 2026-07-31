# Hardware and Software Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current task and execute a special subroutine called an interrupt service routine (ISR).
- The ISR performs the necessary actions to handle the interrupt and then returns control to the original program.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.

## Hardware Interrupts

- Hardware interrupts are caused by external devices that are connected to the microprocessor through dedicated pins.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR.
- NMI stands for non-maskable interrupt and it has the highest priority among all interrupts. It cannot be disabled or ignored by the microprocessor. It is usually used for critical events such as power failure, memory parity error, etc.
- INTR stands for interrupt request and it is a maskable interrupt that can be enabled or disabled by the microprocessor using the interrupt enable (IF) flag in the flags register. It has a lower priority than NMI and it is used for normal events such as keyboard input, disk access, timer output, etc.
- When a hardware interrupt occurs, the microprocessor completes the current instruction and then checks the interrupt pins. If NMI is active, it immediately jumps to the ISR at a fixed address of 0000:0002H. If INTR is active and the IF flag is set, it sends an interrupt acknowledge (INTA) signal to the external device and receives an 8-bit interrupt vector from it. The interrupt vector is used to form the address of the ISR in the interrupt vector table (IVT) located at 0000:0000H to 0000:03FFH. The microprocessor then pushes the flags, CS and IP registers onto the stack and jumps to the ISR. After the ISR is executed, the microprocessor pops the IP, CS and flags registers from the stack and resumes the original program   .

## Software Interrupts

- Software interrupts are caused by program instructions that are executed by the microprocessor.
- The 8086 microprocessor supports 256 software interrupts, numbered from 0 to 255. Each software interrupt has a corresponding interrupt vector in the IVT.
- The software interrupts are invoked by using the INT instruction followed by an 8-bit interrupt number. For example, INT 21H invokes the software interrupt 21H.
- When a software interrupt occurs, the microprocessor behaves similarly to a hardware interrupt, except that it does not check the interrupt pins or send the INTA signal. It simply pushes the flags, CS and IP registers onto the stack and jumps to the ISR using the interrupt vector from the IVT. After the ISR is executed, the microprocessor pops the IP, CS and flags registers from the stack and resumes the original program   .

## References

: https://physicsteacher.in/2022/04/21/interrupts-in-8086-microprocessor-faqs/
: https://www.tutorialspoint.com/microprocessor/microprocessor_8086_interrupts.htm
: https://www.brainkart.com/article/Interrupts-and-Interrupt-Routines-in-8086-Microprocessor_7854/
: https://www.geeksforgeeks.org/interrupts-in-8086-microprocessor/
: https://www.geeksforgeeks.org/difference-between-hardware-interrupt-and-software-interrupt/