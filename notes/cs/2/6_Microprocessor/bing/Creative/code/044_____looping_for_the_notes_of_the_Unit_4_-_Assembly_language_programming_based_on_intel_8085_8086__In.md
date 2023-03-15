### Looping

- Looping is a technique of repeating a block of statements until a condition is satisfied.
- Looping is useful for performing tasks that require iteration, such as counting, indexing, programming techniques, counters and time delays.
- Looping can be implemented in assembly language using the JMP instruction or the LOOP instruction.
- The JMP instruction is used to unconditionally jump to a specified label. The label identifies the target instruction to be executed next.
- The LOOP instruction is used to conditionally jump to a specified label based on the value of the ECX register. The ECX register contains the loop count, which is the number of times the loop body should be executed.
- The LOOP instruction decrements the ECX register by one and jumps to the label if the ECX register is not zero. Otherwise, it continues with the next instruction after the LOOP instruction.
- The syntax of the JMP instruction is:

```
JMP label
```

- The syntax of the LOOP instruction is:

```
LOOP label
```

- An example of a loop using the JMP instruction is:

```
MOV CX, 10 ; initialize loop count to 10
L1:        ; loop label
; loop body
JMP L1     ; jump to loop label
```

- An example of a loop using the LOOP instruction is:

```
MOV ECX, 10 ; initialize loop count to 10
L1:         ; loop label
; loop body
LOOP L1     ; loop to label if ECX is not zero
```

- The LOOP instruction is more convenient and efficient than the JMP instruction for implementing loops, as it does not require an explicit comparison or decrement operation. However, the LOOP instruction can only use the ECX register as the loop count, whereas the JMP instruction can use any register or memory location as the loop condition.