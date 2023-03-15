# Branch Operations

Branch operations are instructions that change the normal flow of execution in a program. They are used to implement control structures such as loops, conditionals, and subroutines. Branch operations can be classified into three types: jump, call, and return.

## Jump Instructions

Jump instructions transfer the program sequence to a specified memory address unconditionally or conditionally based on the status of certain flags. The syntax of a jump instruction is:

```asm
JMP label ; unconditional jump
Jcc label ; conditional jump
```

where `label` is the destination address and `cc` is a condition code that specifies which flag to test. For example, `JZ` means jump if zero flag is set, `JNZ` means jump if zero flag is reset, `JC` means jump if carry flag is set, and so on. There are 16 possible condition codes for jump instructions.

Some examples of jump instructions are:

```asm
JMP LOOP ; jump to the address labeled as LOOP
JZ DONE ; jump to the address labeled as DONE if zero flag is set
JNC SKIP ; jump to the address labeled as SKIP if carry flag is reset
```

## Call Instructions

Call instructions transfer the program sequence to a subroutine, which is a block of code that performs a specific task and returns to the caller. Call instructions save the return address (the address of the next instruction after the call) on the stack, and then jump to the destination address. The syntax of a call instruction is:

```asm
CALL label ; unconditional call
Ccc label ; conditional call
```

where `label` is the address of the subroutine and `cc` is a condition code that specifies which flag to test. The condition codes are the same as for jump instructions.

Some examples of call instructions are:

```asm
CALL SUB ; call the subroutine labeled as SUB
CZ SUB ; call the subroutine labeled as SUB if zero flag is set
CNC SUB ; call the subroutine labeled as SUB if carry flag is reset
```

## Return Instructions

Return instructions transfer the program sequence back to the caller of a subroutine. Return instructions pop the return address from the stack, and then jump to that address. The syntax of a return instruction is:

```asm
RET ; unconditional return
Rcc ; conditional return
```

where `cc` is a condition code that specifies which flag to test. The condition codes are the same as for jump and call instructions.

Some examples of return instructions are:

```asm
RET ; return from a subroutine
RZ ; return from a subroutine if zero flag is set
RNC ; return from a subroutine if carry flag is reset
```

## Looping, Counting, and Indexing

Looping is a technique of repeating a block of code until a certain condition is met. Counting is a technique of keeping track of how many times a loop is executed. Indexing is a technique of accessing elements of an array or a string using a variable that increments or decrements with each iteration of the loop.

Some examples of looping, counting, and indexing are:

```asm
; loop 10 times and print the value of CX
MOV CX, 10 ; initialize the counter
LOOP1:     ; start of the loop
  PRINT CX ; print the value of CX
  DEC CX   ; decrement the counter
  JNZ LOOP1 ; repeat the loop if CX is not zero

; loop through an array of 5 bytes and add them to AL
MOV SI, OFFSET ARRAY ; initialize the index
MOV CX, 5 ; initialize the counter
MOV AL, 0 ; initialize the accumulator
LOOP2:     ; start of the loop
  ADD AL, [SI] ; add the element at SI to AL
  INC SI   ; increment the index
  DEC CX   ; decrement the counter
  JNZ LOOP2 ; repeat the loop if CX is not zero

; loop through a string and count the number of 'A's
MOV SI, OFFSET STR ; initialize the index
MOV CX, 0 ; initialize the counter
LOOP3:     ; start of the loop
  MOV AL, [SI] ; load the character at SI to AL
  CMP AL, '$' ; compare AL with the end of string marker
  JE DONE ; exit the loop if AL is '$'
  CMP AL, 'A' ; compare AL with 'A'
  JNE SKIP ; skip the increment if AL is not 'A'
  INC CX   ; increment the counter
SKIP:      ; skip label
  INC SI