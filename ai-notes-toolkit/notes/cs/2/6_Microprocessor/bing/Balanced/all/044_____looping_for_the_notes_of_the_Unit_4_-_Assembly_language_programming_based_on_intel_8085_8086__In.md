# Looping in Assembly Language Programming

- Looping is a technique that allows a block of statements to be executed repeatedly until a condition is satisfied.
- Looping is useful for performing tasks such as counting, indexing, programming techniques, counters and time delays.
- The assembly language uses the JMP instruction to implement loops. The JMP instruction transfers the control to a specified label unconditionally.
- However, the processor set can also use the LOOP instruction to implement loops conveniently. The LOOP instruction decrements the ECX register and jumps to the specified label unless the ECX register is zero  .
- The LOOP instruction assumes that the ECX register contains the loop count. The loop count is the number of times the loop body is executed.
- The loop body is the block of statements that are repeated in the loop. The loop body should be placed between the label and the LOOP instruction.
- The loop body should not alter the ECX register value, unless it is intended to terminate the loop prematurely.
- The loop body can also contain conditional jumps to exit the loop or to skip some statements based on some conditions.
- The loop body can also contain nested loops, which are loops inside another loop. The nested loops should use different registers for their loop counts, such as EBX, EDX, etc.
- The following is an example of a loop that prints the numbers from 1 to 10 using the INT 21H service:

```assembly
mov ECX, 10 ; loop count
mov AH, 2 ; service to print a character
mov DL, '0' ; initial character
label: ; loop label
add DL, 1 ; increment character
int 21H ; print character
loop label ; repeat loop
```

- The following is an example of a nested loop that prints a 5x5 matrix of asterisks using the INT 21H service:

```assembly
mov ECX, 5 ; outer loop count
outer: ; outer loop label
mov EDX, 5 ; inner loop count
inner: ; inner loop label
mov AH, 2 ; service to print a character
mov DL, '*' ; character to print
int 21H ; print character
dec EDX ; decrement inner loop count
jnz inner ; repeat inner loop if not zero
mov DL, 10 ; line feed character
int 21H ; print line feed
mov DL, 13 ; carriage return character
int 21H ; print carriage return
loop outer ; repeat outer loop
```