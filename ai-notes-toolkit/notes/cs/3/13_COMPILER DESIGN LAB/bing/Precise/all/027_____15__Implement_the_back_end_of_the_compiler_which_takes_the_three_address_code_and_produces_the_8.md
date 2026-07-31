### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

The back end of a compiler is responsible for generating the target code from the intermediate code. In this case, the target code is the 8086 assembly language and the intermediate code is the three address code.

Here are the steps to implement the back end of the compiler:

1. **Translate the three address code into assembly instructions**: Each three address code instruction can be translated into one or more assembly instructions. The translation process involves mapping the operations and operands of the three address code to the corresponding assembly instructions and registers.

2. **Optimize the generated assembly code**: The assembly code generated in the previous step can be further optimized to improve its performance. This can be done by applying techniques such as instruction scheduling, register allocation, and peephole optimization.

3. **Generate the final assembly code**: The optimized assembly code is then assembled into the final 8086 assembly language code. This involves resolving symbolic addresses and generating the machine code.

In summary, the back end of the compiler takes the three address code as input and produces the 8086 assembly language as output by translating the intermediate code into assembly instructions, optimizing the generated code, and generating the final assembly code.