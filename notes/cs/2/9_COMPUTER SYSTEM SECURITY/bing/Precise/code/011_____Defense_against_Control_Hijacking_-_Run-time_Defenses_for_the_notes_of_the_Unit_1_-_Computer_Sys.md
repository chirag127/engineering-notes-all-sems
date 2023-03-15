### Defense against Control Hijacking - Run-time Defenses

Run-time defenses are techniques that aim to prevent control hijacking attacks during the execution of a program. These defenses can be implemented in the operating system, the compiler, or the application itself. Some of the common run-time defenses are:

1. **Address Space Layout Randomization (ASLR)**: This technique randomizes the memory addresses used by the program, making it difficult for an attacker to predict the location of specific code or data.

2. **Stack Canaries**: This technique places a small integer, known as a canary, on the stack before the return address. The canary is checked before a function returns, and if it has been modified, the program is terminated.

3. **Non-Executable Memory**: This technique marks certain regions of memory as non-executable, preventing the execution of code from these regions.

4. **Control Flow Integrity (CFI)**: This technique ensures that the control flow of the program follows a pre-determined path, preventing an attacker from redirecting the control flow to malicious code.

These are some of the common run-time defenses used to prevent control hijacking attacks. It is important to note that no single defense is foolproof, and a combination of techniques is often used to provide the best protection.