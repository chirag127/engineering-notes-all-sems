# Defense against Control Hijacking - Platform Defenses

## Unit 1 - Computer System Security Introduction

### COMPUTER SYSTEM SECURITY

- Control hijacking is a type of attack where an attacker takes control of a program by exploiting a vulnerability in the code.
- Platform defenses are measures implemented at the operating system or hardware level to prevent control hijacking attacks.
- Some common platform defenses include:
  - **Address Space Layout Randomization (ASLR)**: This technique randomizes the memory layout of a program, making it difficult for an attacker to predict the location of code and data.
  - **Data Execution Prevention (DEP)**: This technique prevents the execution of code from data memory regions, making it difficult for an attacker to inject and execute malicious code.
  - **Stack Canaries**: This technique places a small value, known as a canary, on the stack before the return address. If the canary is overwritten, it indicates that a buffer overflow has occurred, and the program can terminate before the attacker gains control.
  - **Control Flow Integrity (CFI)**: This technique ensures that the control flow of a program follows a predefined path, making it difficult for an attacker to hijack the control flow.
- These platform defenses can be effective in preventing control hijacking attacks, but they are not foolproof and can be bypassed by determined attackers.
- It is important to combine platform defenses with other security measures, such as secure coding practices and regular software updates, to provide comprehensive protection against control hijacking attacks.