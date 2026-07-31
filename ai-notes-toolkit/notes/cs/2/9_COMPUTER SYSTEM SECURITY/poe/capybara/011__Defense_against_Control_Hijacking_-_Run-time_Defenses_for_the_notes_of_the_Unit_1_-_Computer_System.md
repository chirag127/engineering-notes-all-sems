### Defense against Control Hijacking - Run-time Defenses

Control Hijacking is a type of attack that is aimed at taking over a computer system by gaining control of its instructions. In order to protect against control hijacking, there are several run-time defenses that can be employed. These defenses are designed to detect and prevent control hijacking attacks.

Here are some of the run-time defenses against control hijacking:

- **Address Space Layout Randomization (ASLR):** ASLR is a technique used to randomize the memory addresses of a program's code and data. This makes it more difficult for an attacker to exploit vulnerabilities in the program, as they cannot predict the location of the code or data they want to hijack.

- **Data Execution Prevention (DEP):** DEP is a security feature that prevents the execution of code from memory that is marked as data. This prevents attackers from executing malicious code that has been injected into a program's data space.

- **Stack Canaries:** Stack canaries are values that are placed on the stack between the return address and local variables. They are used to detect buffer overflow attacks, which can be used to hijack control of a program. When the function returns, the canary value is checked to ensure that it has not been overwritten.

- **Control Flow Integrity (CFI):** CFI is a technique that verifies that the control flow of a program follows a predetermined set of rules. This prevents attackers from hijacking control of the program by redirecting the flow of execution to a different part of the code.

- **Code Signing:** Code signing is a technique that is used to verify the authenticity of code before it is executed. This prevents attackers from injecting malicious code into a program and hijacking control of it.

By employing these run-time defenses, computer systems can be protected against control hijacking attacks. These defenses are designed to detect and prevent attacks at run-time, making them a valuable tool in the fight against cybercrime.