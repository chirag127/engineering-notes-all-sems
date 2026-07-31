### Instruction sets for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram and internal architecture of 8085 microprocessor
  - The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has a 16-bit address bus that can address up to 64 KB of memory. It has 40 pins and operates with +5V power supply.
  - The pin diagram of 8085 microprocessor is shown below   :

  ```
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | A15 | A14 | A13 | A12 | A11 | A10 | A9  | A8  | A7  | A6  | A5  | A4  | A3  | A2  | A1  | A0  |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |  13 |  14 |  15 |  16 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | AD0 | AD1 | AD2 | AD3 | AD4 | AD5 | AD6 | AD7 | VCC | S0  | S1  | IO/M| RD  | WR  | ALE | X1  |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  17 |  18 |  19 |  20 |  21 |  22 |  23 |  24 |  25 |  26 |  27 |  28 |  29 |  30 |  31 |  32 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | X2  | RESET OUT | RESET IN | CLK OUT | READY | HOLD | HLDA | INTR | INTA | TRAP | RST 7.5 | RST 6.5 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  33 |     34    |    35    |   36    |  37   |  38  |  39  |  40  |  41  |  42  |   43    |   44    |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | RST 5.5 | SID | SOD | VSS |
  +-----+-----+-----+-----+-----+
  |   45    | 46  | 47  | 48  |
  +-----+-----+-----+-----+-----+
  ```

  - The internal architecture of 8085 microprocessor consists of various units such as :
    - CPU: The central processing unit is the core of the microprocessor that executes the instructions and performs the operations. It has the following components:
      - Instruction register and decoder: It holds the current instruction and decodes it into control signals for other units.
      - Timing and control unit: It generates the timing and control signals for the internal and external operations of the microprocessor.
      - Registers