### Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or redirect the execution to existing code in the program or the system.
- The goal of control hijacking is to gain unauthorized access, privilege escalation, data theft, denial of service, or other malicious actions.
- Some common types of control hijacking attacks are:
  - Buffer overflow attacks: The attacker overwrites the memory beyond the allocated space of a buffer, which may contain return addresses, function pointers, or other control data. The attacker can then overwrite these data with the address of the malicious code or a system function.
  - Integer overflow attacks: The attacker exploits a flaw in the arithmetic operations of the program, such as adding or multiplying two large numbers, which may result in a negative or truncated value. The attacker can then use this value to manipulate the memory allocation, array indexing, or loop termination.
  - Format string attacks: The attacker exploits a flaw in the use of format specifiers in the printf function or its variants, which may allow the attacker to read or write arbitrary memory locations. The attacker can then use this ability to leak sensitive information or overwrite control data.
- Some common defenses against control hijacking are:
  - Input validation: The program should check the length and format of the input data before processing it, and reject any invalid or suspicious input.
  - Code randomization: The program or the system should randomize the memory layout of the code segments, such as the stack, the heap, or the libraries, to make it harder for the attacker to predict the address of the malicious code or the system function.
  - Stack protection: The program should use a canary value, such as a random number or a checksum, to detect any modification of the return address or the stack frame. The program should also use a non-executable stack, which prevents the execution of any code on the stack.
  - Ciphering the packets: The network should encrypt the packets sent between the server and the client, to prevent the attacker from intercepting or cracking the session tokens or other sensitive information.