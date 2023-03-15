# Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or data into the program's memory and manipulate the program counter or return address to execute the injected code or data.
- Control hijacking can compromise the confidentiality, integrity, and availability of the system and the data stored or processed by the program.
- Some common types of control hijacking attacks are:
  - Buffer overflow attacks: The attacker overwrites the buffer boundaries and corrupts the adjacent memory locations, such as the return address or the stack frame pointer. The attacker can then redirect the execution to the malicious code or data injected into the buffer or another memory location.
  - Integer overflow attacks: The attacker exploits an arithmetic operation that results in a value that is too large or too small to be stored in the allocated memory space. This can cause unexpected behavior, such as truncation, wrap-around, or sign extension, and lead to memory corruption or incorrect branching.
  - Format string attacks: The attacker exploits a format string vulnerability, which occurs when a program passes user input as a format string to a function that performs formatted output, such as printf. The attacker can use format specifiers to read or write arbitrary memory locations, or to execute arbitrary code.
- Some possible defenses against control hijacking attacks are:
  - Input validation: The program checks the input for any malicious or unexpected characters, length, or format before processing it. This can prevent the attacker from injecting malicious code or data into the program's memory.
  - Ciphering: The program encrypts the data or the packets sent over the network, so that the attacker cannot decipher them or modify them in transit . This can prevent the attacker from intercepting or spoofing the communication or the session .
  - Runtime checking: The program uses techniques such as stack canaries, address space layout randomization, or non-executable memory to detect or prevent the modification of the control flow or the execution of injected code or data . This can prevent the attacker from hijacking the control of the program .