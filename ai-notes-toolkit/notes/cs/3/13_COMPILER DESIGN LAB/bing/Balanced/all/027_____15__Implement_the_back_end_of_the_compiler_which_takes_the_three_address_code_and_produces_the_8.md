### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

- The back end of the compiler is the part that generates the target code from the intermediate code, such as the three address code (TAC).
- The 8086 assembly language is a low-level programming language for the Intel 8086 microprocessor, which has a 16-bit architecture and supports 8-bit and 16-bit data types.
- To implement the back end of the compiler, the following steps are required:

  - Define the target code format and instruction set. The target code format specifies how the assembly language instructions, operands, labels, directives, and comments are written. The instruction set defines the available operations and their syntax and semantics. For example, the target code format for the 8086 assembly language is:

    ```
    [label:] mnemonic [operands] [;comment]
    ```

    The instruction set for the 8086 assembly language includes arithmetic, logical, data transfer, control transfer, string, and miscellaneous instructions. For example, the instruction `ADD AX, BX` adds the contents of the registers AX and BX and stores the result in AX.

  - Define the target code generation rules. The target code generation rules specify how to translate each TAC instruction into one or more target code instructions. The rules depend on the source language features, the target machine architecture, and the optimization goals. For example, the rule for translating the TAC instruction `x = y + z` into the 8086 assembly language is:

    ```
    MOV AX, y ;move the value of y to AX
    ADD AX, z ;add the value of z to AX
    MOV x, AX ;move the value of AX to x
    ```

  - Implement the target code generator. The target code generator is the module that applies the target code generation rules to each TAC instruction and produces the corresponding target code instructions. The target code generator can be implemented using various techniques, such as table-driven, syntax-directed, or pattern-matching methods. For example, the target code generator can use a table that maps each TAC operator to a corresponding target code instruction, and then generate the target code operands based on the TAC operands. Alternatively, the target code generator can use a syntax-directed method that traverses the abstract syntax tree of the TAC and generates the target code instructions based on the attributes of the nodes.