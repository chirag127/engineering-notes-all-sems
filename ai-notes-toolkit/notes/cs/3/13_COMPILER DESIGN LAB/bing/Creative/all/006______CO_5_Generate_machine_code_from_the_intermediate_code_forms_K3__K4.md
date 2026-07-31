#### CO 5 Generate machine code from the intermediate code forms K3, K4

- Machine code is the low-level binary representation of a program that can be directly executed by the target system.
- Intermediate code is a high-level or abstract representation of a program that is independent of the target system  .
- Intermediate code generation is the process of translating the source code into intermediate code by the compiler  .
- Machine code generation is the process of translating the intermediate code into machine code by the code generator  .
- The advantages of using intermediate code are:
  - It enhances the portability of the compiler, as the same intermediate code can be used for different target systems .
  - It simplifies the code generation and optimization phases, as the intermediate code is more structured and uniform than the source code .
- The challenges of generating machine code from intermediate code are:
  - The code generator has to deal with the limited number of registers and memory locations available in the target system .
  - The code generator has to map the intermediate code instructions to the corresponding machine code instructions, which may not have a one-to-one correspondence .
  - The code generator has to handle the differences in the instruction formats, operands, addressing modes, and control flow structures between the intermediate code and the machine code .
- The steps involved in generating machine code from intermediate code are:
  - Instruction selection: The code generator chooses the appropriate machine code instructions for each intermediate code instruction .
  - Register allocation: The code generator assigns the intermediate code operands to the available registers or memory locations in the target system .
  - Instruction scheduling: The code generator orders the machine code instructions to optimize the performance and reduce the stalls in the target system .
- The types of intermediate code forms are:
  - K3: Three-address code, which is a linear sequence of instructions, each having at most three operands .
  - K4: Quadruples, which is a table of four columns, each representing an operator, an argument, another argument, and a result .
- The examples of generating machine code from intermediate code forms are:

  | Intermediate code (K3) | Machine code |
  | ---------------------- | ------------ |
  | x = y + z              | ADD R1, y    |
  |                        | ADD R1, z    |
  |                        | MOV x, R1    |
  | if x < y goto L1       | CMP x, y     |
  |                        | JL L1        |
  | L1: x = x + 1          | L1: INC x    |

  | Intermediate code (K4) | Machine code |
  | ---------------------- | ------------ |
  | (+, y, z, t1)          | ADD R1, y    |
  |                        | ADD R1, z    |
  |                        | MOV t1, R1   |
  | (<, x, y, t2)          | CMP x, y     |
  |                        | SETL R2      |
  |                        | MOV t2, R2   |
  | (goto, t2, -, L1)      | TEST t2      |
  |                        | JNZ L1       |
  | (L1, =, t1, x)         | L1: MOV x, t1|