### Looping

- Looping is a technique of repeating a block of statements until a condition is satisfied.
- Looping is useful for performing tasks that require iteration, such as counting, indexing, programming techniques, counters and time delays.
- Looping can be implemented in assembly language using the JMP instruction or the LOOP instruction.
- The JMP instruction is a conditional or unconditional jump to a specified label. The label identifies the target instruction to be executed next.
- The LOOP instruction is a special instruction that decrements the ECX register and jumps to a specified label unless the ECX register is zero. The ECX register acts as the loop counter.
- The syntax of the JMP instruction is:

  ```
  JMP condition label
  ```

  where condition is an optional flag that specifies the condition for the jump, and label is the target label.

- The syntax of the LOOP instruction is:

  ```
  LOOP label
  ```

  where label is the target label.

- An example of a loop using the JMP instruction is:

  ```
  MOV CX, 10 ; initialize the loop counter to 10
  L1:        ; loop label
  ; loop body
  DEC CX     ; decrement the loop counter
  JNZ L1     ; jump to L1 if the loop counter is not zero
  ```

- An example of a loop using the LOOP instruction is:

  ```
  MOV ECX, 10 ; initialize the loop counter to 10
  L1:         ; loop label
  ; loop body
  LOOP L1     ; decrement the loop counter and jump to L1 if not zero
  ```