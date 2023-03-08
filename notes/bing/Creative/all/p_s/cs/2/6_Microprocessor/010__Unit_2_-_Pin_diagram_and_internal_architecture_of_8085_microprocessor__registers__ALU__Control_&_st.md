## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- The 8085 microprocessor is an 8-bit microprocessor that was introduced by Intel in 1976 using NMOS technology  .
- It is software-binary compatible with the Intel 8080, with only two minor instructions added to support its added interrupt and serial input/output features.
- It has the following configuration:
  - 8-bit data bus
  - 16-bit address bus, which can address up to 64KB
  - A 16-bit program counter
  - A 16-bit stack pointer
  - Six 8-bit registers arranged in pairs: BC, DE, HL
  - An 8-bit accumulator
  - An 8-bit temporary register
  - Five flags: Sign, Zero, Auxiliary Carry, Parity, Carry
  - An instruction register and a decoder
  - A timing and control unit
  - An interrupt control unit
  - A serial input/output control unit
- The pin diagram of the 8085 microprocessor is shown below:

```
       +-----+--+-----+
  AD0  |1    +--+  40 | Vcc
  AD1  |2         39 | AD7
  AD2  |3         38 | AD6
  AD3  |4         37 | AD5
  AD4  |5         36 | AD4
  AD5  |6         35 | RST 7.5
  AD6  |7         34 | RST 6.5
  AD7  |8         33 | RST 5.5
  ALE  |9         32 | IO/M
  RD   |10        31 | S0
  WR   |11        30 | S1
  READY|12        29 | SID
  HOLD |13        28 | SOD
  HLDA |14        27 | INTA
  RESET IN|15     26 | TRAP
  RESET OUT|16    25 | RST 7.5
  CLK OUT|17      24 | INTR
  X1   |18        23 | X2
  X2   |19        22 | GND
  Vss  |20        21 | CLK IN
       +------------+
```

- The internal architecture of the 8085 microprocessor is shown below:

```
       +-----------------+    +-----------------+
       |                 |    |                 |
       |    Accumulator  |    |   Program      |
       |                 |    |   Counter      |
       |                 |    |                 |
       +-----------------+    +-----------------+
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |                     |
                 |

Some possible mnemonics and learning tricks for the topic are:

- To remember the names of the six 8-bit registers, you can use the acronym **B**ad **D**ogs **H**ave **L**ice, which stands for **B**C, **D**E, **H**L.
- To remember the names of the five flags, you can use the acronym **S**ome **Z**ebras **A**re **P**retty **C**ute, which stands for **S**ign, **Z**ero, **A**uxiliary Carry, **P**arity, **C**arry.
- To remember the functions of the three control signals S0, S1 and IO/M, you can use the table below:

| S0 | S1 | IO/M | Function |
|----|----|------|----------|
| 0  | 0  | 0    | Halt     |
| 0  | 0  | 1    | Memory read |
| 0  | 1  | 0    | Write    |
| 0  | 1  | 1    | I/O read |
| 1  | 0  | 0    | No operation |
| 1  | 0  | 1    | Memory write |
| 1  | 1  | 0    | Latch address |
| 1  | 1  | 1    | I/O write |

- To remember the order of the seven interrupts, you can use the acronym **T**rap **R**ats **I**n **S**ix **F**ive **F**our, which stands for **T**RAP, **R**ST 7.5, **I**NTR, **R**ST 6.5, **R**ST 5.5, **R**ST 4.5.