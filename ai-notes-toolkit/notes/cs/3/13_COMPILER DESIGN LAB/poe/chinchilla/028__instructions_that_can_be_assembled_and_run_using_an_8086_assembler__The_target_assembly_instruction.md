### Instructions That Can Be Assembled and Run Using an 8086 Assembler

An assembler is a program that converts assembly language into machine code, which can be executed directly by the computer's CPU. The 8086 is a popular microprocessor architecture that was widely used in the 1980s and early 1990s. Here are some instructions that can be assembled and run using an 8086 assembler:

1. Move (MOV): The MOV instruction is used to move data from one location to another. It has the following syntax: 

    ```
    MOV destination, source
    ```

    For example, to move the value 10 into the AX register, you would use the following instruction:

    ```
    MOV AX, 10
    ```

2. Add (ADD): The ADD instruction is used to add two values together. It has the following syntax:

    ```
    ADD destination, source
    ```

    For example, to add the value in the BX register to the value in the AX register and store the result in the DX register, you would use the following instruction:

    ```
    ADD DX, BX
    ```

3. Subtract (SUB): The SUB instruction is used to subtract one value from another. It has the following syntax:

    ```
    SUB destination, source
    ```

    For example, to subtract the value in the CX register from the value in the AX register and store the result in the BX register, you would use the following instruction:

    ```
    SUB BX, CX
    ```

4. Compare (CMP): The CMP instruction is used to compare two values. It has the following syntax:

    ```
    CMP operand1, operand2
    ```

    For example, to compare the value in the AX register to the value 5, you would use the following instruction:

    ```
    CMP AX, 5
    ```

5. Jump (JMP): The JMP instruction is used to jump to a different part of the program. It has the following syntax:

    ```
    JMP label
    ```

    For example, to jump to the label "END" at the end of the program, you would use the following instruction:

    ```
    JMP END
    ```

These are just a few of the many instructions that can be assembled and run using an 8086 assembler. By learning these basic instructions, you can start to write simple programs in assembly language and gain a better understanding of how computer systems work at a low level.