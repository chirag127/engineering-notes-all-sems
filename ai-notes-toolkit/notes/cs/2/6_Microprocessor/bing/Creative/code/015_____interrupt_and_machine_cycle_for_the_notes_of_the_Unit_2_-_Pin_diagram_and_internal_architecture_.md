# Interrupt and Machine Cycle for the Notes of the Unit 2

## Interrupts in 8085 Microprocessor

- An interrupt is a signal that causes the microprocessor to temporarily stop its current program execution and switch to a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are initiated by external devices that are connected to the microprocessor through the interrupt pins. The 8085 microprocessor has five hardware interrupt pins: INTR, RST 7.5, RST 6.5, RST 5.5, and TRAP   .
- Software interrupts are instructions that are inserted in the program to generate an interrupt. The 8085 microprocessor has eight software interrupt instructions: RST 0, RST 1, RST 2, RST 3, RST 4, RST 5, RST 6, and RST 7.
- The interrupt signals have different priorities, which determine the order in which they are serviced by the microprocessor. The highest priority interrupt is TRAP, followed by RST 7.5, RST 6.5, RST 5.5, and INTR   .
- The microprocessor can enable or disable the interrupts using the EI (enable interrupt) and DI (disable interrupt) instructions. The interrupts can also be masked or unmasked using the SIM (set interrupt mask) and RIM (read interrupt mask) instructions   .
- When an interrupt is accepted by the microprocessor, it performs the following steps   :
  - It completes the execution of the current instruction.
  - It saves the address of the next instruction on the stack.
  - It sends an interrupt acknowledge signal (INTA) to the interrupting device.
  - It receives the interrupt vector (a byte that specifies the address of the ISR) from the device or the instruction.
  - It jumps to the ISR and executes it.
  - It returns to the main program by popping the saved address from the stack.

## Machine Cycles in 8085 Microprocessor

- A machine cycle is the basic unit of time required by the microprocessor to perform an operation. It consists of one or more clock cycles (T-states), which are the smallest units of time in the microprocessor.
- The 8085 microprocessor has six types of machine cycles: opcode fetch, memory read, memory write, I/O read, I/O write, and interrupt acknowledge .
- The opcode fetch cycle is used to fetch the opcode of an instruction from the memory. It consists of four T-states: T1, T2, T3, and T4. In T1 and T2, the microprocessor places the address of the instruction on the address bus and enables the memory read signal. In T3, the microprocessor reads the opcode from the data bus and increments the program counter. In T4, the microprocessor decodes the opcode and prepares for the next cycle .
- The memory read cycle is used to read data from the memory. It consists of three T-states: T1, T2, and T3. In T1 and T2, the microprocessor places the address of the data on the address bus and enables the memory read signal. In T3, the microprocessor reads the data from the data bus and stores it in a register or a memory location .
- The memory write cycle is used to write data to the memory. It consists of three T-states: T1, T2, and T3. In T1 and T2, the microprocessor places the address of the data on the address bus and the data on the data bus. In T3, the microprocessor enables the memory write signal and writes the data to the memory .
- The I/O read cycle is used to read data from an input device. It consists of three T-states: T1, T2, and T3. In T1 and T2, the microprocessor places the address of the device on the address bus and enables the I/O read signal. In