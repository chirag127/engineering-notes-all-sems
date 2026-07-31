# Interrupt and Machine Cycle

## Interrupt
- An interrupt is a signal that causes the microprocessor to temporarily stop its current program execution and switch to a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are initiated by external devices that are connected to the microprocessor through the interrupt pins. The 8085 microprocessor has five interrupt pins: INTR, RST 7.5, RST 6.5, RST 5.5, and TRAP .
- Software interrupts are instructions that are inserted in the program to generate an interrupt. The 8085 microprocessor has eight software interrupts: RST 0, RST 1, RST 2, RST 3, RST 4, RST 5, RST 6, and RST 7.
- Interrupts can be enabled or disabled by using the EI (enable interrupt) and DI (disable interrupt) instructions. The microprocessor also has a flip-flop called the interrupt enable flip-flop (IEF) that controls the interrupt acceptance. The EI instruction sets the IEF to 1, while the DI instruction resets it to 0.
- When an interrupt is accepted, the microprocessor performs the following steps :
  - It completes the execution of the current instruction.
  - It saves the address of the next instruction on the stack.
  - It sends an interrupt acknowledge signal (INTA) to the interrupting device.
  - It receives the interrupt vector (a predefined address of the ISR) from the interrupting device or from the instruction itself.
  - It jumps to the ISR and executes it.
  - It returns to the main program by popping the saved address from the stack.

## Machine Cycle
- A machine cycle is the basic operation performed by the microprocessor to execute an instruction. It consists of one or more clock cycles (T-states) during which the microprocessor accesses the memory or the I/O devices.
- The 8085 microprocessor has six types of machine cycles: opcode fetch, memory read, memory write, I/O read, I/O write, and interrupt acknowledge .
- The opcode fetch cycle is the first cycle of every instruction. It is used to fetch the opcode (the binary code of the instruction) from the memory. It consists of four T-states: T1, T2, T3, and T4. During this cycle, the microprocessor performs the following operations :
  - It places the address of the instruction on the address bus (A15-A0) and enables the ALE (address latch enable) signal to latch the address in the external latch.
  - It enables the RD (read) signal to indicate that it is reading from the memory.
  - It receives the opcode from the data bus (D7-D0) and stores it in the instruction register (IR).
  - It increments the program counter (PC) by one to point to the next instruction.
- The memory read cycle is used to read data from the memory. It consists of three T-states: T1, T2, and T3. During this cycle, the microprocessor performs the following operations :
  - It places the address of the data on the address bus (A15-A0) and enables the ALE signal to latch the address in the external latch.
  - It enables the RD signal to indicate that it is reading from the memory.
  - It receives the data from the data bus (D7-D0) and stores it in the accumulator (A) or another register.
- The memory write cycle is used to write data to the memory. It consists of three T-states: T1, T2, and T3. During this cycle, the microprocessor performs the following operations :
  - It places the address of the data on the address bus (A15-A0) and enables the ALE signal to latch the address in the external latch.
  - It enables the WR (write) signal to indicate that it is writing to the memory.
  - It places the data from the accumulator (A) or another register on the data bus (D7-D0) and sends it to the memory.
- The I/O read cycle is used to read data from an I/O device. It consists of three T-states