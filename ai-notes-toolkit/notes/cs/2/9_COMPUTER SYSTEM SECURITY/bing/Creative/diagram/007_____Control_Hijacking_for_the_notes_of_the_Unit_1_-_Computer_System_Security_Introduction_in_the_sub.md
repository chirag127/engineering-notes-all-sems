### Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or redirect the execution to existing code in the program or the system libraries.
- The goal of control hijacking is to execute arbitrary code or commands on the target system, such as opening a shell, stealing data, deleting files, etc.
- Some common techniques of control hijacking are:
  - Buffer overflow attacks: The attacker overwrites the return address or a function pointer on the stack or the heap with the address of the malicious code or a gadget .
  - Integer overflow attacks: The attacker exploits an arithmetic operation that results in a value that is too large or too small to be stored in a variable, causing a memory allocation error or a boundary check bypass.
  - Format string attacks: The attacker exploits a printf-like function that takes a user-supplied format string as an argument, allowing the attacker to read or write arbitrary memory locations.
- Some possible defenses against control hijacking are:
  - Ciphering the packets: This prevents the attacker from deciphering the packet headers or the session tokens, which can aid in spoofing or hijacking .
  - Stack canaries: This is a value placed on the stack before the return address, which is checked before returning from a function. If the canary is corrupted, the program aborts.
  - Address space layout randomization (ASLR): This is a technique that randomizes the location of the code, data, stack, and heap segments in the memory, making it harder for the attacker to predict the addresses of the malicious code or the gadgets.
  - Non-executable memory: This is a mechanism that marks certain memory regions as non-executable, preventing the attacker from running code from the stack or the heap.