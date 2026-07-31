 Here is the formal content in Markdown format without any emojis or external links:

### Pin diagram and internal architecture of 8085 microprocessor

* It is a 8-bit microprocessor that is compatible with its predecessor 8080.
* It has 40 pins and uses +5V single supply.
* The pin diagram consists of following:
** Address bus - It has 16 pins to address 64K memory locations.
** Data bus - It has 8 pins to transfer 8-bit data.
** Control bus - It consists of 4 pins namely WR, RD, M1 and MREQ to perform read/write operation from/to memory/I/O devices.
** Interrupt pins - It has INT, RST 5.5 and RST 6.5 pins to handle interrupt requests.
** Clock signal - It has pin 18 to provide clock pulses.
** Supply pins - It consists of VCC and GND pins to provide power supply.

* The internal architecture consists of following major blocks:
** Instruction decoder and machine cycle generator - It interprets and executes instructions.
** Registers - It consists of 6 registers to hold 8-bit data and addresses.
** ALU - It performs arithmetic and logical operations on 8-bit data.
** Control and status unit - It controls signals for communication between internal blocks. It has flag registers to indicate status.
** Interrupt control - It controls interrupt requests of various priority levels.

* The microprocessor executes instructions in machine cycles consisting of following steps:
** Fetch - It fetches instruction from memory.
** Decode - It decodes the instruction.
** Execute - It executes the instruction.

* The instructions can be classified into:
** Data transfer - MOV, MVI, LDA
** Arithmetic - ADD, SUB, INR, DCR
** Logical - ORA, ANI, XRI
** Branching - JMP, JNZ, JZ, JNC, JC
** Machine control - HLT, PCHL
** Assembler directives - EQU, ORG

* The instructions can use different addressing modes to access operands.