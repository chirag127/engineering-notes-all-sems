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
  | AD7 | AD6 | AD5 | AD4 | AD3 | AD2 | AD1 | AD0 | ALE | IO/M| S0  | S1  | RD  | WR  | READY| HOLD|
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  17 |  18 |  19 |  20 |  21 |  22 |  23 |  24 |  25 |  26 |  27 |  28 |  29 |  30 |  31 |  32 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | HLDA| RESET IN| RESET OUT| CLK OUT| X2 | X1 | VSS | SID | SOD | TRAP| RST 7.5| RST 6.5| RST 5.5| INTR| INTA| VCC |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  33 |   34    |    35    |   36   | 37 | 38 | 39  | 40  | 39  | 38  |   37   |   36   |   35   |  34 |  33 |  32 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  ```
  - The internal architecture of 8085 microprocessor consists of various units such as registers, ALU, control and status, interrupt and machine cycle. The CPU acts as the core of the microprocessor and it has instruction register and decoder, timing control, various registers, and serial I/O control. The internal architecture of 8085 microprocessor is shown below:

  ```
  +-----------------+     +-----------------+     +-----------------+     +-----------------+
  |                 |     |                 |     |                 |     |                 |
  |    Address      |     |    Data Bus     |     |    Control      |     |    Power        |

```
