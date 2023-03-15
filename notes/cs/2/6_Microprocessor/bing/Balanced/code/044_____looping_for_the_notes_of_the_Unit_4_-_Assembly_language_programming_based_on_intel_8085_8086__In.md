### Looping

- Looping is a technique of repeating a block of statements until a condition is satisfied.
- Looping is useful for performing tasks that require iteration, such as counting, indexing, programming techniques, counters and timers.
- Looping can be implemented in assembly language using the JMP instruction or the LOOP instruction.

#### JMP Instruction

- The JMP instruction is used to transfer the control to a specified label unconditionally.
- The JMP instruction has the following syntax: `JMP label`
- The label is the target instruction that identifies the loop body.
- The JMP instruction can be used to implement loops by using a register or a memory location to store the loop counter and decrementing it in each iteration.
- The JMP instruction can also be used to implement conditional loops by using the Jcc instructions, such as JE, JNE, JL, JG, etc.
- The Jcc instructions are used to transfer the control to a specified label if a condition is met based on the flags register.
- The Jcc instructions have the following syntax: `Jcc label`
- The label is the target instruction that identifies the loop body.
- The condition is based on the flags register, such as ZF, CF, SF, OF, etc.
- For example, the following code snippet implements a loop that prints "Hello" 10 times using the JMP instruction:

```assembly
mov cx, 10 ; initialize the loop counter
loop_start: ; loop label
    mov dx, offset msg ; load the message address
    mov ah, 09h ; print string service
    int 21h ; invoke DOS interrupt
    dec cx ; decrement the loop counter
    jnz loop_start ; jump to loop label if cx is not zero
    jmp exit ; exit the program
msg db "Hello", 0Dh, 0Ah, "$" ; message to print
exit: ; exit label
    mov ah, 4Ch ; terminate program service
    int 21h ; invoke DOS interrupt
```

#### LOOP Instruction

- The LOOP instruction is a special instruction that is used to implement loops conveniently.
- The LOOP instruction has the following syntax: `LOOP label`
- The label is the target instruction that identifies the loop body.
- The LOOP instruction assumes that the ECX register contains the loop counter.
- When the LOOP instruction is executed, the ECX register is decremented and the control jumps to the target label, until the ECX register value, i.e., the counter reaches the value zero.
- The LOOP instruction can be used to implement simple loops that do not require any condition checking.
- For example, the following code snippet implements the same loop as above using the LOOP instruction:

```assembly
mov ecx, 10 ; initialize the loop counter
loop_start: ; loop label
    mov dx, offset msg ; load the message address
    mov ah, 09h ; print string service
    int 21h ; invoke DOS interrupt
    loop loop_start ; loop until ecx is zero
    jmp exit ; exit the program
msg db "Hello", 0Dh, 0Ah, "$" ; message to print
exit: ; exit label
    mov ah, 4Ch ; terminate program service
    int 21h ; invoke DOS interrupt
```

- The LOOP instruction can also be combined with other instructions to implement conditional loops, such as LOOPE, LOOPNE, LOOPZ, and LOOPNZ.
- The LOOPE and LOOPZ instructions are used to loop until ECX is zero or the ZF flag is zero, i.e., the last comparison was equal.
- The LOOPNE and LOOPNZ instructions are used to loop until ECX is zero or the ZF flag is one, i.e., the last comparison was not equal.
- The LOOPE, LOOPNE, LOOPZ, and LOOPNZ instructions have the following syntax: `LOOPE label`, `LOOPNE label`, `LOOPZ label`, and `LOOPNZ label`
- The label is the target instruction that identifies the loop body.
- For example, the following code snippet implements a loop that searches for a character in a string using the LOOPE instruction:

```assembly
mov ecx, len ; initialize the loop counter with the string length
mov al, 'a' ; character to search
mov si, offset str ; load the string address
loop_start: ; loop label
    cmp al, [si] ; compare the character with the string element
    je found ; jump to found label if equal
    inc si ; increment the string pointer