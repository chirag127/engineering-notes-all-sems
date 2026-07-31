### Defense against Control Hijacking - Run-time Defenses

Run-time defenses are techniques that aim to prevent control hijacking attacks during the execution of a program. These defenses can be implemented in the operating system, the compiler, or the program itself. Some of the common run-time defenses are:

1. **Address Space Layout Randomization (ASLR)**: This technique randomizes the memory layout of a program, making it difficult for an attacker to predict the location of code and data in memory. This makes it harder for an attacker to exploit vulnerabilities such as buffer overflows.

2. **Data Execution Prevention (DEP)**: This technique prevents the execution of code from data memory regions, such as the stack and the heap. This makes it harder for an attacker to inject and execute malicious code.

3. **Stack Canaries**: This technique places a small value, known as a canary, on the stack before the return address. The canary value is checked before a function returns, and if it has been modified, the program is terminated. This makes it harder for an attacker to overwrite the return address and hijack the control flow of the program.

4. **Control Flow Integrity (CFI)**: This technique ensures that the control flow of a program follows a pre-determined path. This makes it harder for an attacker to hijack the control flow of the program by modifying function pointers or return addresses.

These are some of the common run-time defenses used to protect against control hijacking attacks. It is important to note that these defenses are not foolproof and can be bypassed by determined attackers. However, they do provide an additional layer of protection and can make it more difficult for attackers to exploit vulnerabilities in a program.