### Branch Operations

Branch operations are instructions that change the normal sequential flow of execution in a program. They are used to implement control structures such as loops, conditionals, subroutines, etc. Branch operations can be classified into three types:

- **Jump instructions**: These instructions transfer the program control to a specified memory address unconditionally or based on a flag condition. The operand of a jump instruction can be an immediate value, a register, or a memory location. The syntax of a jump instruction is:

  ```
  JMP label
  ```

  or

  ```
  Jcc label
  ```

  where `label` is the destination address and `cc` is a flag condition such as `Z` (zero), `NZ` (not zero), `C` (carry), `NC` (no carry), etc. For example:

  ```
  JMP LOOP ; unconditional jump to LOOP
  JZ DONE ; jump to DONE if zero flag is set
  ```

- **Call instructions**: These instructions transfer the program control to a subroutine, which is a block of code that performs a specific task and returns to the caller. The return address of the caller is pushed onto the stack before the call instruction is executed. The syntax of a call instruction is:

  ```
  CALL label
  ```

  or

  ```
  Ccc label
  ```

  where `label` is the address of the subroutine and `cc` is a flag condition. For example:

  ```
  CALL SUM ; call the subroutine SUM
  CNZ ERROR ; call the subroutine ERROR if not zero flag is set
  ```

- **Return instructions**: These instructions return the program control to the caller of a subroutine. The return address is popped from the stack and loaded into the program counter. The syntax of a return instruction is:

  ```
  RET
  ```

  or

  ```
  Rcc
  ```

  where `cc` is a flag condition. For example:

  ```
  RET ; return to the caller
  RC ; return if carry flag is set
  ```