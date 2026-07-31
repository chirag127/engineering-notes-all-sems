Hello, I am Sydney, your AI assistant. I can help you with your topic.

### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

- The back end of the compiler is the part that generates the target code from the intermediate code, such as the three address code (TAC).
- The 8086 assembly language is a low-level programming language for the Intel 8086 microprocessor, which has a 16-bit architecture and supports 256 instructions.
- To implement the back end of the compiler, we need to perform the following steps:

  1. Define the target machine model, which specifies the registers, memory, addressing modes, instruction set, and instruction format of the 8086 processor.
  2. Define the mapping of TAC operators and operands to 8086 instructions and operands, which may involve some transformations, such as converting arithmetic expressions to stack operations, or introducing temporary variables.
  3. Define the register allocation and assignment strategy, which decides how to use the available registers to store the TAC operands, and how to handle spilling and reloading when the registers are not enough.
  4. Define the code generation algorithm, which traverses the TAC and generates the corresponding 8086 instructions, following the mapping and the register allocation and assignment strategy.
  5. Define the code optimization techniques, which aim to improve the quality and efficiency of the generated code, such as eliminating redundant instructions, reducing memory accesses, or rearranging the code sequence.

- Here is an example of how to implement the back end of the compiler for a simple TAC statement:

  - TAC: `a = b + c`
  - Target machine model: The 8086 processor has 14 registers, 8 general-purpose registers (AX, BX, CX, DX, SI, DI, BP, SP), and 6 segment registers (CS, DS, ES, SS, FS, GS). The memory is divided into segments of 64 KB each, and each segment has a base address and an offset. The addressing modes are register, immediate, direct, register indirect, based, indexed, and based indexed. The instruction set supports arithmetic, logical, data transfer, control transfer, string, and miscellaneous instructions. The instruction format consists of an opcode, a mod-reg field, a reg field, an r/m field, a displacement, and an immediate data.
  - Mapping: The TAC operator `+` can be mapped to the 8086 instruction `ADD`, which adds the source operand to the destination operand and stores the result in the destination operand. The TAC operands `a`, `b`, and `c` can be mapped to the 8086 operands, which can be registers, memory locations, or immediate values.
  - Register allocation and assignment: A possible strategy is to use the general-purpose registers to store the TAC operands, and assign them in the order of AX, BX, CX, DX, SI, DI, BP, SP. If the registers are not enough, we can use the memory locations to store the spilled operands, and use the segment registers to access them. For example, we can use DS as the data segment, and use an offset to locate the spilled operand. We can also use the stack to store and retrieve the spilled operands, and use SP as the stack pointer, and BP as the base pointer.
  - Code generation: A possible algorithm is to scan the TAC from left to right, and generate the 8086 instructions according to the mapping and the register allocation and assignment strategy. For example, for the TAC statement `a = b + c`, we can generate the following 8086 instructions:

    ```
    MOV AX, b ; move the value of b to AX
    ADD AX, c ; add the value of c to AX
    MOV a, AX ; move the value of AX to a
    ```

  - Code optimization: A possible technique is to use the common subexpression elimination, which identifies and eliminates the repeated computations of the same expression. For example, if we have another TAC statement `d = b + c`, we can avoid computing `b + c` again, and reuse the value in AX. We can generate the following 8086 instructions:

    ```
    MOV AX, b ; move the value of b to AX
    ADD AX, c ; add the value of c to AX
    MOV a, AX ; move the value of AX to a
    MOV d, AX ; move the value of AX to d
    ```