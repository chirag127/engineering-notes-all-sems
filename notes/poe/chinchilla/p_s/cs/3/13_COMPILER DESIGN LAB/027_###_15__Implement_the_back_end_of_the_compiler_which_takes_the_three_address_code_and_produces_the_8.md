### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language.

Compiler is a software that converts the source code written in one language to another language. The process of converting the source code to machine code comprises of different stages, also known as phases of the compiler. The last phase of compiler is known as the back end phase, which is responsible for generating the target code.

In this topic, we will focus on the implementation of the back end of the compiler, which takes the three address code as input and produces the 8086 assembly language. Here are the key points that will help you understand the concept in a better way:

#### Three Address Code:

- Three address code is a type of intermediate code representation that is used by compilers to generate the target code.
- The three address code has instructions that operate on three operands, where each operand can be a constant, variable or expression.
- The basic structure of three address code is: `x := y op z`, where `x`, `y` and `z` are operands and `op` is the operator.

#### 8086 Assembly Language:

- 8086 assembly language is a low-level programming language that is used to write programs for the Intel 8086 microprocessor.
- The 8086 assembly language is a symbolic representation of machine code that is executed by the processor.
- The 8086 assembly language has instructions that operate on registers and memory locations.

#### Back End Phase:

- The back end phase of compiler is responsible for generating the target code from the intermediate code (three address code).
- The back end phase consists of three stages: code generation, code optimization and code emission.
- The code generation stage maps each intermediate code instruction to one or more target code instructions.
- The code optimization stage analyzes the generated code and tries to improve its efficiency by reducing the number of instructions or by replacing complex instructions with simpler ones.
- The code emission stage outputs the final target code in the desired format (in this case, 8086 assembly language).

#### Implementation:

- To implement the back end of the compiler, we need to write a code generator that maps each three address code instruction to one or more 8086 assembly language instructions.
- We also need to write an optimizer that analyzes the generated code and tries to optimize it for better performance.
- Finally, we need to write a code emitter that outputs the optimized target code in the desired format (8086 assembly language).

#### Advantages:

- The back end phase of compiler is responsible for generating efficient and optimized target code from the intermediate code.
- The 8086 assembly language is a low-level programming language that provides direct access to the hardware resources of the processor, making it suitable for writing device drivers and system-level programs.

#### Disadvantages:

- Writing a code generator and optimizer for the back end phase of compiler is a complex and time-consuming task.
- The generated code may not be portable and may only work on specific hardware platforms.

#### Example:

Here is an example of a three address code instruction and its corresponding 8086 assembly language instructions:

Three address code: `x := y + z`

8086 assembly language:

```
MOV AX, Y
ADD AX, Z
MOV X, AX
```

#### Applications:

- The back end phase of compiler is used in various software development tools, such as compilers, interpreters, and assemblers.
- The 8086 assembly language is still used in some embedded systems and device drivers.