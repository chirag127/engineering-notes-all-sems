# ALU

- ALU stands for Arithmetic and Logic Unit. It is a functional unit of the 8085 microprocessor that performs arithmetic, logical, and bitwise operations on 8-bit data .
- ALU is connected to the internal data bus and the accumulator register. The accumulator is an 8-bit register that stores one of the operands and the result of the operation .
- ALU can perform the following operations  :
  - Addition and subtraction of two 8-bit numbers, with or without carry/borrow.
  - Increment and decrement of an 8-bit number by one.
  - Logical AND, OR, XOR, and NOT of two 8-bit numbers.
  - Bitwise shift and rotate of an 8-bit number, left or right, with or without carry.
  - Compare two 8-bit numbers and set the flags accordingly.
- ALU also sets the flags in the flag register according to the result of the operation. The flag register is a 5-bit register that indicates the status of the ALU and the microprocessor  .
- The flags are as follows  :
  - S (Sign) flag: Set if the result is negative, i.e., the most significant bit is 1.
  - Z (Zero) flag: Set if the result is zero, i.e., all the bits are 0.
  - AC (Auxiliary Carry) flag: Set if there is a carry/borrow from the lower nibble (4 bits) to the higher nibble during addition/subtraction.
  - P (Parity) flag: Set if the result has an even number of 1 bits, i.e., the parity is even.
  - CY (Carry) flag: Set if there is a carry/borrow from the most significant bit during addition/subtraction.
- ALU is implemented using a combination of logic gates, multiplexers, adders, and shifters. The 8085 ALU uses a novel technique called "serial-parallel" arithmetic, which allows it to perform operations in a single cycle by using a carry-lookahead adder and a serial shifter.
- ALU is one of the most important components of the 8085 microprocessor, as it enables the microprocessor to perform various computations and manipulations on data. ALU is also responsible for setting the flags that control the flow of the program and the execution of conditional instructions.