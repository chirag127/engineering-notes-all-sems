### Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or redirect the execution to existing code in the program or the system.
- The goal of control hijacking is to gain unauthorized access, privilege escalation, data theft, denial of service, or other malicious actions.
- Some common types of control hijacking attacks are:
  - Buffer overflow attacks: The attacker overwrites the memory beyond the allocated buffer size, causing the program to crash or execute arbitrary code. Buffer overflow attacks can be classified into stack-based or heap-based, depending on the location of the buffer.
  - Integer overflow attacks: The attacker exploits a flaw in the arithmetic operations of the program, causing the result to exceed the maximum or minimum value that can be stored in an integer variable. This can lead to memory corruption, incorrect branching, or code execution.
  - Format string attacks: The attacker exploits a vulnerability in the use of format specifiers in printf-like functions, causing the program to read or write arbitrary memory locations or execute arbitrary code.
  - Session hijacking attacks: The attacker intercepts or cracks the session tokens that are used to authenticate the user on a web server, causing the server to grant access to the attacker as the legitimate user.
- Some possible defenses against control hijacking attacks are:
  - Input validation: The program should check the length and format of the input data before processing it, and reject any invalid or suspicious input.
  - Encryption: The program should encrypt the data and the session tokens that are transmitted over the network, so that the attacker cannot read or modify them.
  - Stack protection: The program should use techniques such as stack canaries, stack cookies, or stack guard to detect and prevent buffer overflow attacks on the stack.
  - Address space layout randomization (ASLR): The program should randomize the location of the code and data segments in the memory, so that the attacker cannot predict the address of the target function or variable.
  - Non-executable memory: The program should mark the memory regions that contain data as non-executable, so that the attacker cannot inject and execute code in them.