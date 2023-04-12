## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram of 8085 microprocessor:

  - The 8085 microprocessor is a 40-pin IC with 8-bit data bus and 16-bit address bus.
  - The pin diagram of 8085 microprocessor is shown below:

    ```
    +-----+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-----+
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Vcc |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A15 |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A14 |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A13 |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A12 |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A11 |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A10 |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |
    | AD7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A9  |
    |     +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+     |
    |     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     |

```
