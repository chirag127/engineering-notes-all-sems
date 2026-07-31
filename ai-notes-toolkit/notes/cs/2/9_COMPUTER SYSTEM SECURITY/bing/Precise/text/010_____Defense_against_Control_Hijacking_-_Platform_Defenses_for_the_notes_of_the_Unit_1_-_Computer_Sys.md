### Defense against Control Hijacking - Platform Defenses

1. **Address Space Layout Randomization (ASLR)**: This technique randomizes the location of the program's code, data, and stack in memory, making it difficult for an attacker to predict the location of these regions and exploit them.

2. **Data Execution Prevention (DEP)**: This technique marks certain regions of memory as non-executable, preventing the execution of code from these regions. This can help prevent attacks that rely on injecting and executing malicious code in data regions.

3. **Stack Canaries**: This technique places a small value, known as a canary, on the stack before the return address. The canary value is checked before the function returns, and if it has been modified, the program will terminate, preventing the attacker from overwriting the return address and hijacking control of the program.

4. **Control Flow Integrity (CFI)**: This technique ensures that the control flow of the program follows a pre-determined path, preventing an attacker from redirecting the control flow to malicious code.

These are some of the platform defenses that can be used to defend against control hijacking attacks. It is important to note that these techniques are not foolproof and can be bypassed by determined attackers. However, they can significantly increase the difficulty of successfully exploiting a vulnerability and can be used in conjunction with other security measures to provide a more robust defense.