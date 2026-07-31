### Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions of a microprocessor  .
- Assembly language is specific to a given processor, so the assembly language of 8085 is different from that of 8086 .
- Assembly language programming involves writing the source code in a text editor, assembling it into an object file, and linking it to generate an executable file.
- The basic format of an assembly language instruction is:

```
[label:] mnemonic [operands] [;comment]
```

- The label is an optional identifier that marks the location of the instruction in memory. The mnemonic is a symbolic name for the operation code (opcode) of the instruction. The operands are the data or addresses used by the instruction. The comment is an optional explanation of the instruction.
- Some examples of assembly language instructions for 8085 are:

```
LDA 2500H ;load the accumulator with the data at address 2500H
MOV B,A ;move the contents of the accumulator to register B
ADD C ;add the contents of register C to the accumulator
JNZ LOOP ;jump to the label LOOP if the zero flag is not set
```

- Some examples of assembly language instructions for 8086 are:

```
MOV AX,1234H ;move the immediate data 1234H to register AX
MOV BX,AX ;move the contents of register AX to register BX
ADD AX,BX ;add the contents of register BX to register AX
JNE LOOP ;jump to the label LOOP if the zero flag is not set
```

- The 8085 microprocessor has a 8-bit data bus and a 16-bit address bus. It can address up to 64 KB of memory. It has 74 instructions and 246 opcodes. It has five 8-bit registers (A, B, C, D, E), one 16-bit register (HL), one 16-bit program counter (PC), one 16-bit stack pointer (SP), and one 8-bit flag register (F)  .
- The 8086 microprocessor has a 16-bit data bus and a 20-bit address bus. It can address up to 1 MB of memory. It has 133 instructions and 300 opcodes. It has eight 16-bit registers (AX, BX, CX, DX, SI, DI, BP, SP), one 16-bit program counter (IP), one 16-bit flag register (FLAGS), and four 16-bit segment registers (CS, DS, SS, ES) .
- The data transfer instructions are used to move data between registers, memory, and I/O devices. Some examples of data transfer instructions for 8085 are:

```
LDA ;load the accumulator from memory
STA ;store the accumulator to memory
MOV ;move data between registers or memory
LXI ;load register pair with immediate data
PUSH ;push register pair onto stack
POP ;pop register pair from stack
IN ;input data from I/O device
OUT ;output data to I/O device
```

- Some examples of data transfer instructions for 8086 are:

```
MOV ;move data between registers, memory, or immediate data
XCHG ;exchange data between registers or memory
PUSH ;push register or memory onto stack
POP ;pop register or memory from stack
IN ;input data from I/O port
OUT ;output data to I/O port
```

- The arithmetic instructions are used to perform addition, subtraction, increment, decrement, multiplication, and division operations on data. Some examples of arithmetic instructions for 8085 are:

```
ADD ;add register or memory to accumulator
ADC ;add register or memory to accumulator with carry
SUB ;subtract register or memory from accumulator
SBB ;subtract register or memory from accumulator with borrow
INR ;increment register or memory by one
DCR ;decrement register or memory by one
DAD ;add register pair to HL register pair
DAA ;decimal adjust accumulator after addition
```

- Some examples of arithmetic instructions for 8086 are:

```
ADD ;add register, memory, or immediate data to register or memory
ADC ;add register, memory, or immediate data to register or memory with carry
SUB ;subtract register, memory

```
