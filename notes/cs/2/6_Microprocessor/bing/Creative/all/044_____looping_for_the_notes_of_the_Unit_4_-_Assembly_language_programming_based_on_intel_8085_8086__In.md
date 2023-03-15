# Looping

- Looping is a technique of repeating a block of statements until a condition is satisfied.
- Looping is useful for performing tasks that require iteration, such as counting, indexing, programming techniques, counters and time delays.
- Looping can be implemented in assembly language using the JMP instruction or the LOOP instruction.

## JMP Instruction

- The JMP instruction is used to transfer the control to a specified label unconditionally.
- The JMP instruction has the following syntax: `JMP label`
- The label is the target instruction that identifies the loop body.
- The JMP instruction can be used to implement loops by using a counter register and a conditional jump instruction.
- The counter register is initialized with the number of iterations before the loop body.
- The conditional jump instruction is used to check the counter register after the loop body and jump back to the loop body if the counter is not zero.
- The conditional jump instruction can be one of the following: JZ, JNZ, JC, JNC, JO, JNO, JS, JNS, etc.
- The conditional jump instruction has the following syntax: `Jcc label`
- The cc is the condition code that specifies the flag to be tested.
- The label is the target instruction that identifies the loop body.
- The following example shows how to implement a loop using the JMP instruction:

```assembly
; loop 10 times
mov cx, 10 ; initialize counter
loop_start: ; loop body
; do something
dec cx ; decrement counter
jnz loop_start ; jump if not zero
```

## LOOP Instruction

- The LOOP instruction is a special instruction that is used to implement loops conveniently.
- The LOOP instruction has the following syntax: `LOOP label`
- The label is the target instruction that identifies the loop body.
- The LOOP instruction assumes that the ECX register contains the loop count.
- The LOOP instruction decrements the ECX register and jumps to the label if the ECX register is not zero.
- The following example shows how to implement a loop using the LOOP instruction:

```assembly
; loop 10 times
mov ecx, 10 ; initialize loop count
loop_start: ; loop body
; do something
loop loop_start ; loop instruction
```