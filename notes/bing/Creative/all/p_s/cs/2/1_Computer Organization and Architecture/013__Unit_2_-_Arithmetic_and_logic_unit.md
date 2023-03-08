## Unit 2 - Arithmetic and logic unit

- An arithmetic and logic unit (ALU) is a major component of the central processing unit (CPU) of a computer system  .
- It performs arithmetic and logic operations on the operands in computer instruction words.
- In some processors, the ALU is divided into two units: an arithmetic unit (AU) and a logic unit (LU)  .
- The AU performs operations such as addition, subtraction, multiplication, division, and shifting .
- The LU performs operations such as AND, OR, XOR, NOT, and comparison .
- The ALU has a set of inputs and outputs that are connected to the CPU and the main memory .
- The inputs include the operands, the operation code, and the control signals .
- The outputs include the result, the carry, the overflow, the zero, and the sign flags .
- The ALU can be implemented using combinational logic circuits such as multiplexers, adders, subtractors, comparators, and shifters  .
- The ALU can also be designed using microprogramming, where a sequence of microinstructions controls the internal operations of the ALU .
- The ALU is a crucial part of the CPU, as it executes the basic operations that are required for most programs .
- The ALU can also be used for other purposes, such as encryption, decryption, hashing, and checksum calculation .

An example of an ALU is shown below:

```
    +-----------------+     +-----------------+
    |                 |     |                 |
    |   Operand A     |     |   Operand B     |
    |                 |     |                 |
    +-----------------+     +-----------------+
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             v                       v
    +-------------------------------------------------+
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                  ALU                           |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    +-------------------------------------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             v
    +-------------------------------------------------+
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                  Result                        |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    +-------------------------------------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             v
    +-------------------------------------------------+
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                  Flags                         |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    |                                                 |
    +-------------------------------------------------+
```

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of operations in arithmetic, use the acronym PEMDAS (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) or BODMAS (Brackets, Orders, Division, Multiplication, Addition, Subtraction).
- To remember the truth tables for the logic gates, use the following phrases:
  - AND: Both must be true
  - OR: Either one or both must be true
  - XOR: Only one must be true
  - NOT: The opposite of the input
- To remember the difference between combinational and sequential logic circuits, use the following analogy:
  - Combinational logic circuits are like calculators: they produce an output based on the current input only.
  - Sequential logic circuits are like clocks: they produce an output based on the current input and the previous state.