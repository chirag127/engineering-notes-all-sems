### Defense against Control Hijacking - Run-time Defenses

Run-time defenses are techniques that aim to prevent control hijacking attacks while a program is running. These defenses can be implemented in the operating system, the compiler, or the program itself. Some common run-time defenses include:

1. **Address Space Layout Randomization (ASLR)**: This technique randomizes the memory layout of a program, making it difficult for an attacker to predict the location of code and data. This makes it harder for an attacker to exploit vulnerabilities that rely on knowing the memory layout of a program.

2. **Data Execution Prevention (DEP)**: This technique prevents the execution of code from data memory regions, such as the stack or the heap. This makes it harder for an attacker to inject and execute malicious code.

3. **Stack Canaries**: This technique places a small value, known as a canary, on the stack before the return address. The canary is checked before a function returns, and if it has been modified, the program will terminate. This makes it harder for an attacker to overwrite the return address and hijack the control flow of the program.

4. **Control Flow Integrity (CFI)**: This technique ensures that the control flow of a program follows a pre-determined path. This makes it harder for an attacker to hijack the control flow of the program by modifying function pointers or return addresses.

These are some of the common run-time defenses used to protect against control hijacking attacks. It is important to note that no single defense is foolproof, and a combination of techniques is often used to provide the best protection.