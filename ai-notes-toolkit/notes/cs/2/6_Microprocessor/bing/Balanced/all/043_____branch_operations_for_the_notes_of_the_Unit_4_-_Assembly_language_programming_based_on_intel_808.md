# Branch Operations

Branch operations are instructions that change the normal sequential flow of execution in a program. They are used to implement control structures such as loops, conditionals, subroutines, etc. Branch operations can be classified into three types:

- **Jump instructions**: These instructions transfer the program control to a specified memory address unconditionally or based on a flag condition. The operand of a jump instruction can be an immediate value, a register, or a memory location. For example, `JMP 1000H` jumps to the address 1000H unconditionally, while `JZ 2000H` jumps to the address 2000H only if the zero flag is set.
- **Call instructions**: These instructions transfer the program control to a subroutine, which is a sequence of instructions that performs a specific task. The call instruction also saves the return address on the stack, so that the program can resume from where it left off after the subroutine is completed. The operand of a call instruction can be an immediate value, a register, or a memory location. For example, `CALL SUB` calls the subroutine named SUB, and pushes the address of the next instruction on the stack.
- **Return instructions**: These instructions transfer the program control back to the main program after a subroutine is finished. The return instruction also pops the return address from the stack, and jumps to that address. The return instruction can be unconditional or conditional based on a flag condition. For example, `RET` returns from a subroutine unconditionally, while `RC` returns only if the carry flag is set.

Some examples of branch operations in assembly language are:

```assembly
; A loop that adds the numbers from 1 to 10 and stores the sum in AX
    MOV AX, 0 ; initialize AX to 0
    MOV CX, 10 ; initialize CX to 10 (loop counter)
LOOP1:
    ADD AX, CX ; add CX to AX
    DEC CX ; decrement CX
    JNZ LOOP1 ; jump to LOOP1 if CX is not zero
    ; AX now contains the sum of 1 to 10
```

```assembly
; A conditional branch that checks if a number in AL is even or odd
    MOV AL, 5 ; initialize AL to 5
    AND AL, 1 ; perform bitwise AND with 1
    JZ EVEN ; jump to EVEN if the result is zero (even number)
    ; otherwise, the number is odd
    ; do something for odd numbers
    JMP END ; jump to END
EVEN:
    ; do something for even numbers
END:
    ; end of program
```