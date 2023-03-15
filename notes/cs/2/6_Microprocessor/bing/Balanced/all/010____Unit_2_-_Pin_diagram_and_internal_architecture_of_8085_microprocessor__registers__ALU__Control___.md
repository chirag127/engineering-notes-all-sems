## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram of 8085 microprocessor:

  - The 8085 microprocessor is a 40-pin IC with 8-bit data bus and 16-bit address bus.
  - The pins can be classified into six groups: address bus, data bus, control and status signals, power supply and frequency, externally initiated signals, and serial I/O ports.
  - The address bus consists of 8 pins (A8-A15) that are multiplexed with the data bus (AD0-AD7) and two pins (A16 and A17) that are used to select the memory bank.
  - The data bus consists of 8 pins (AD0-AD7) that are bidirectional and multiplexed with the lower 8 bits of the address bus (A0-A7).
  - The control and status signals consist of 6 pins: RD (read), WR (write), IO/M (input/output or memory), S0 and S1 (status), and ALE (address latch enable).
  - The power supply and frequency pins consist of 2 pins: Vcc (+5V) and Vss (ground), and one pin: X1/X2 (clock input).
  - The externally initiated signals consist of 5 pins: RESET IN (reset input), RESET OUT (reset output), HOLD (hold request), HLDA (hold acknowledge), and READY (ready).
  - The serial I/O ports consist of 2 pins: SID (serial input data) and SOD (serial output data).

- Internal architecture of 8085 microprocessor:

  - The 8085 microprocessor consists of three main units: arithmetic and logic unit (ALU), registers, and control unit.
  - The ALU performs arithmetic and logical operations on 8-bit data. It has an accumulator (A) register, a temporary (T) register, and a flag (F) register. The flag register contains five flags: sign (S), zero (Z), auxiliary carry (AC), parity (P), and carry (C).
  - The registers are used to store data and addresses. They include six general purpose registers: B, C, D, E, H, and L, which can be used as pairs (BC, DE, HL) or individually. They also include two special purpose registers: program counter (PC) and stack pointer (SP), which store 16-bit addresses. The PC points to the next instruction to be executed, and the SP points to the top of the stack in memory.
  - The control unit generates control and timing signals for the internal and external operations of the microprocessor. It has an instruction register (IR), an instruction decoder, and a timing and control unit. The IR holds the current instruction, the instruction decoder decodes the instruction and generates the appropriate signals, and the timing and control unit synchronizes the operations with the clock.

- Instruction sets:

  - The 8085 microprocessor has 246 instructions, which can be classified into five groups: data transfer, arithmetic, logical, branching, and machine control.
  - The data transfer instructions are used to move data between registers, memory, and I/O devices. They include instructions such as MOV, MVI, LXI, LDA, STA, LHLD, SHLD, LDAX, STAX, XCHG, etc.
  - The arithmetic instructions are used to perform arithmetic operations on 8-bit or 16-bit data. They include instructions such as ADD, ADC, SUB, SBB, INR, DCR, INX, DCX, DAD, etc.
  - The logical instructions are used to perform logical operations on 8-bit data. They include instructions such as ANA, ORA, XRA, CMP, RLC, RRC, RAL, RAR, CMA, CMC, STC, etc.
  - The branching instructions are used to alter the sequence of execution of the program based on certain conditions. They include instructions such as JMP, JNZ, JZ, JNC, JC, JPO, JPE, JN, JP, CALL, RET, RST, etc.
  - The machine control instructions are used to control the operation of the microprocessor and the peripheral devices. They include instructions such as HLT, NOP, DI, EI, SIM, RIM, etc.

- Addressing modes:

  - The 8085 microprocessor has five addressing modes