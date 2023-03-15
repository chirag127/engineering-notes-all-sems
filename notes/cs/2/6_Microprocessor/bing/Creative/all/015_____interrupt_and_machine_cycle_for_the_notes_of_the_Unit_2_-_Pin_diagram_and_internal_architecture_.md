# Interrupt and Machine Cycle

## Interrupt
- An interrupt is a signal that causes the microprocessor to temporarily stop its current program execution and switch to a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be initiated by external devices or by software instructions.
- Interrupts are useful for handling events that require immediate attention, such as keyboard input, timer overflow, or hardware errors.
- The 8085 microprocessor has five hardware interrupt pins: INTR, RST 7.5, RST 6.5, RST 5.5, and TRAP.
- The 8085 microprocessor also has eight software interrupt instructions: RST 0, RST 1, RST 2, RST 3, RST 4, RST 5, RST 6, and RST 7.
- The hardware interrupts have different priorities, with TRAP being the highest and INTR being the lowest.
- The software interrupts have fixed vector addresses, with RST 0 being 0000H and RST 7 being 0038H.
- The interrupt process involves the following steps:
  - The microprocessor checks the interrupt lines after each instruction execution.
  - If an interrupt request is detected, the microprocessor completes the current instruction and sends an interrupt acknowledge signal (INTA) to the requesting device.
  - The device sends an 8-bit instruction (usually a CALL or RST) to the microprocessor through the data bus.
  - The microprocessor saves the address of the next instruction on the stack and executes the received instruction.
  - The microprocessor jumps to the ISR and performs the required tasks.
  - The microprocessor returns to the main program by popping the saved address from the stack and executing a RET instruction.

## Machine Cycle
- A machine cycle is the basic operation performed by the microprocessor to access memory or I/O devices.
- A machine cycle consists of one or more clock cycles (T-states), during which the microprocessor performs certain operations such as fetching, decoding, executing, or writing an instruction or data.
- The 8085 microprocessor has five types of machine cycles: Opcode Fetch, Memory Read, Memory Write, I/O Read, and I/O Write.
- The Opcode Fetch cycle is used to fetch the opcode of an instruction from the memory. It consists of four T-states: T1, T2, T3, and T4.
  - In T1, the microprocessor places the address of the instruction on the address bus and enables the memory read signal (MEMR).
  - In T2, the microprocessor receives the opcode from the memory through the data bus and increments the program counter (PC).
  - In T3, the microprocessor decodes the opcode and prepares for the next cycle.
  - In T4, the microprocessor performs an internal operation and completes the cycle.
- The Memory Read cycle is used to read data from the memory. It consists of three T-states: T1, T2, and T3.
  - In T1, the microprocessor places the address of the data on the address bus and enables the memory read signal (MEMR).
  - In T2, the microprocessor receives the data from the memory through the data bus and stores it in the appropriate register.
  - In T3, the microprocessor performs an internal operation and completes the cycle.
- The Memory Write cycle is used to write data to the memory. It consists of three T-states: T1, T2, and T3.
  - In T1, the microprocessor places the address of the data on the address bus and enables the memory write signal (MEMW).
  - In T2, the microprocessor places the data on the data bus and sends it to the memory.
  - In T3, the microprocessor performs an internal operation and completes the cycle.
- The I/O Read cycle is used to read data from an I/O device. It consists of three T-states: T1, T2, and T3.
  - In T1, the microprocessor places the address of the I/O device on the address bus and enables the I/O read signal (IOR).
  - In T2, the microprocessor receives the data from the I/O device through the data bus and stores it in the accumulator (A).
  - In T3, the microprocessor performs an internal operation and completes the cycle.
- The I