# Addresses in the Target Code

- Addresses in the target code are the locations where the values of the variables, constants, temporaries, and parameters are stored in the memory or registers of the target machine.
- The code generator is responsible for assigning addresses to the operands of the three-address code and generating the target code accordingly.
- There are different types of addresses in the target code, such as absolute addresses, relative addresses, indirect addresses, and register addresses.
- Absolute addresses are the actual memory locations where the operands are stored. For example, x:= y + z can be translated to the target code:

```
LD R1, 1000 // load the value of y from memory location 1000 to register R1
LD R2, 2000 // load the value of z from memory location 2000 to register R2
ADD R1, R1, R2 // add the values of R1 and R2 and store the result in R1
ST R1, 3000 // store the value of R1 to memory location 3000, which is the address of x
```

- Relative addresses are the offsets from a base address, such as the beginning of the activation record or the stack pointer. For example, x:= y + z can be translated to the target code:

```
LD R1, 8(SP) // load the value of y from the offset 8 from the stack pointer to register R1
LD R2, 12(SP) // load the value of z from the offset 12 from the stack pointer to register R2
ADD R1, R1, R2 // add the values of R1 and R2 and store the result in R1
ST R1, 4(SP) // store the value of R1 to the offset 4 from the stack pointer, which is the address of x
```

- Indirect addresses are the addresses that contain the actual addresses of the operands. They are useful for implementing pointers, arrays, and dynamic memory allocation. For example, x:= y + z can be translated to the target code:

```
LD R1, 1000 // load the value of y from memory location 1000 to register R1
LD R2, 2000 // load the value of z from memory location 2000 to register R2
ADD R1, R1, R2 // add the values of R1 and R2 and store the result in R1
LD R3, 3000 // load the value of x from memory location 3000 to register R3
ST R1, (R3) // store the value of R1 to the memory location pointed by R3
```

- Register addresses are the names of the registers where the operands are stored. They are the most efficient way of accessing the operands, as they do not require any memory access. For example, x:= y + z can be translated to the target code:

```
MOV R1, R2 // move the value of y from register R2 to register R1
ADD R1, R1, R3 // add the values of R1 and R3 and store the result in R1
MOV R4, R1 // move the value of R1 to register R4, which is the address of x
```

- The code generator can use different strategies for allocating registers to the operands, such as static allocation, usage counts, graph coloring, and live-range analysis. The code generator can also perform optimizations on the target code, such as common subexpression elimination, constant folding, dead code elimination, and loop invariant code motion.