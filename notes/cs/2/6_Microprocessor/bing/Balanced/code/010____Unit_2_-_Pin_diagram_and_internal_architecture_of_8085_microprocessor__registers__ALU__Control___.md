## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram of 8085 microprocessor:

  - The 8085 microprocessor is a 40-pin IC with 8-bit data bus and 16-bit address bus.
  - The pins can be classified into six groups: address bus, data bus, control and status signals, power supply and frequency, externally initiated signals, and serial I/O ports.
  - The address bus consists of 8 multiplexed pins (AD0-AD7) and 8 non-multiplexed pins (A8-A15). The multiplexed pins carry both address and data during different phases of a machine cycle. The non-multiplexed pins carry only the higher order address bits.
  - The data bus consists of 8 bidirectional pins (AD0-AD7) that carry data to and from the microprocessor. The data bus is buffered and tristated to allow interfacing with other devices.
  - The control and status signals consist of 6 pins that control the operation of the microprocessor and indicate its status. They are: ALE (Address Latch Enable), RD (Read), WR (Write), IO/M (Input/Output or Memory), S0 and S1 (Status signals).
  - The power supply and frequency pins provide the necessary voltage and clock signals for the microprocessor. They are: Vcc (+5V), Vss (Ground), X1 and X2 (Crystal or R/C network), CLK (OUT) (Clock output), and RESET (IN) (Reset input).
  - The externally initiated signals consist of 5 pins that allow external devices to interrupt or reset the microprocessor. They are: TRAP (Non-maskable interrupt), RST 7.5, RST 6.5, RST 5.5 (Maskable interrupts), and INTR (Interrupt request).
  - The serial I/O ports consist of 2 pins that allow serial communication with other devices. They are: SID (Serial input data) and SOD (Serial output data).

- Internal architecture of 8085 microprocessor:

  - The 8085 microprocessor consists of three main units: the arithmetic and logic unit (ALU), the register array, and the control unit.
  - The ALU performs arithmetic and logical operations on 8-bit data. It also sets the flags in the flag register according to the result of the operation. The flags are: S (Sign), Z (Zero), AC (Auxiliary carry), P (Parity), and CY (Carry).
  - The register array consists of six general purpose registers (B, C, D, E, H, and L), one accumulator (A), one flag register (F), one program counter (PC), and one stack pointer (SP). The general purpose registers can be used as 8-bit registers or as 16-bit register pairs (BC, DE, and HL). The accumulator is used to store the result of the ALU operations. The flag register is used to store the status flags. The program counter is used to store the address of the next instruction to be executed. The stack pointer is used to store the address of the top of the stack in memory.
  - The control unit generates the control and timing signals for the microprocessor and the external devices. It also decodes the instructions and generates the appropriate signals for the ALU and the register array. The control unit consists of an instruction register (IR), an instruction decoder, a timing and control circuit, and an interrupt control circuit.

- Registers:

  - A register is a small and fast memory unit that can store data temporarily. Registers are used to hold operands, intermediate results, addresses, and control information during the execution of a program.
  - The 8085 microprocessor has 12 registers: six general purpose registers (B, C, D, E, H, and L), one accumulator (A), one flag register (F), one program counter (PC), one stack pointer (SP), one instruction register (IR), and one temporary register (W).
  - The general purpose registers can be used for data manipulation and address calculation. They can be used as 8-bit registers or as 16-bit register pairs (BC, DE, and HL).
  - The accumulator is the main register of the microprocessor. It is used to store the result of the ALU operations and to perform input/output operations. It can also be used as an operand for some instructions.