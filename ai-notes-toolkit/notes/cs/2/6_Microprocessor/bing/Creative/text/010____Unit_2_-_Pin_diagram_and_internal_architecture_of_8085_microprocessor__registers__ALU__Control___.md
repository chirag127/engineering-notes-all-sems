## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram of 8085 microprocessor:

  - The 8085 microprocessor is a 40-pin IC with 8-bit data bus and 16-bit address bus.
  - The pins can be classified into six groups: address bus, data bus, control and status signals, power supply and frequency, externally initiated signals, and serial I/O ports.
  - The address bus consists of 8 pins (A8-A15) that are multiplexed with the data bus (AD0-AD7) and two pins (A16 and ALE) that are used for address latch enable and higher order address bits.
  - The data bus consists of 8 pins (AD0-AD7) that are bidirectional and multiplexed with the lower order address bits (A0-A7).
  - The control and status signals consist of 6 pins that are used to synchronize and control the operations of the microprocessor and the peripheral devices. They are: RD (read), WR (write), IO/M (input/output or memory), S0 and S1 (status), and READY (ready).
  - The power supply and frequency pins consist of 3 pins that are used to provide the operating voltage and clock signal to the microprocessor. They are: Vcc (+5V), Vss (ground), and X1 and X2 (crystal or R/C network).
  - The externally initiated signals consist of 5 pins that are used to communicate with external devices and handle interrupts and resets. They are: INTA (interrupt acknowledge), INTR (interrupt request), RST 5.5, RST 6.5, RST 7.5 (maskable interrupts), TRAP (non-maskable interrupt), and RESET IN and RESET OUT (reset signals).
  - The serial I/O ports consist of 2 pins that are used to perform serial data communication using the SID (serial input data) and SOD (serial output data) pins.

- Internal architecture of 8085 microprocessor:

  - The 8085 microprocessor consists of three main units: the arithmetic and logic unit (ALU), the timing and control unit, and the register array.
  - The ALU performs arithmetic and logical operations on 8-bit data and also generates flags to indicate the status of the result. The flags are: S (sign), Z (zero), AC (auxiliary carry), P (parity), and CY (carry).
  - The timing and control unit generates and coordinates the timing signals and control signals for the internal and external operations of the microprocessor. It also handles the interrupt and serial I/O operations.
  - The register array consists of six general purpose registers (B, C, D, E, H, and L), one accumulator (A), one program counter (PC), one stack pointer (SP), and one temporary register (W). The general purpose registers can be used as 8-bit registers or as 16-bit register pairs (BC, DE, and HL). The accumulator is used to store the result of the ALU operations. The program counter is used to store the address of the next instruction to be executed. The stack pointer is used to store the address of the top of the stack. The temporary register is used to store intermediate results during some operations.

- Instruction sets of 8085 microprocessor:

  - The 8085 microprocessor supports 246 instructions that can be classified into five categories: data transfer, arithmetic, logical, branching, and machine control.
  - The data transfer instructions are used to move data between registers, memory, and I/O devices. They include: MOV, MVI, LXI, LDA, STA, LHLD, SHLD, LDAX, STAX, XCHG, PUSH, POP, IN, and OUT.
  - The arithmetic instructions are used to perform addition, subtraction, increment, and decrement operations on 8-bit or 16-bit data. They include: ADD, ADC, SUB, SBB, INR, DCR, INX, DCX, DAD, and DAA.
  - The logical instructions are used to perform bitwise logical operations on 8-bit data. They include: ANA, ORA, XRA, CMP, RLC, RRC, RAL, RAR, CMA, CMC, and STC.
  - The branching instructions are used to alter the sequence of execution based on certain conditions or flags.