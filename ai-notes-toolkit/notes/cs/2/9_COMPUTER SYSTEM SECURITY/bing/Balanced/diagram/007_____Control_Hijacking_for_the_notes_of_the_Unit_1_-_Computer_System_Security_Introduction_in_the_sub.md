### Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or redirect the execution to existing code in the program or the system.
- The goal of control hijacking is to gain unauthorized access, escalate privileges, execute commands, steal data, or cause denial of service.
- Some common techniques of control hijacking are:
  - Buffer overflow: The attacker overwrites the return address or a function pointer on the stack or the heap with the address of the malicious code or a gadget .
  - Integer overflow: The attacker exploits an arithmetic operation that results in a value that is too large or too small to be stored in a variable, causing a memory allocation error or a boundary check bypass.
  - Format string: The attacker exploits a printf-like function that takes a user-supplied format string as an argument, allowing the attacker to read or write arbitrary memory locations.
- Some possible defenses against control hijacking are:
  - Ciphering the packets: This prevents the attacker from deciphering the packet headers or the session tokens, which can be used to spoof the identity or hijack the session.
  - Stackguard: This is a compiler technique that inserts a canary value between the local variables and the return address on the stack, and checks the integrity of the canary before returning from the function .
  - Address space layout randomization (ASLR): This is a system technique that randomizes the base address of the executable, the stack, the heap, and the libraries, making it harder for the attacker to guess the address of the malicious code or a gadget .
  - Non-executable memory: This is a hardware technique that marks some memory regions as non-executable, preventing the attacker from executing code on the stack or the heap .