### Advanced Control Hijacking Attacks

- A control hijacking attack is carried out by overwriting part of the data structures of a victim program, causing it to lose control of its control flow and, as a result, the program's and perhaps the underlying system's control .
- A control hijacking attack exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- Control-hijacking attacks are also known as control-flow hijacking attacks.
- Some examples of control hijacking attacks are:
  - Buffer overflow attacks: The attacker overwrites the return address or a function pointer on the stack or the heap with a malicious address, causing the program to jump to that address and execute arbitrary code .
  - Return-oriented programming (ROP) attacks: The attacker chains together short code snippets (called gadgets) that end with a return instruction, and overwrites the return address on the stack with the address of the first gadget, causing the program to execute the gadgets in sequence.
  - RDP hijacking attacks: The attacker logs into a remote desktop protocol (RDP) server and takes over the session of another user, gaining access to their desktop and applications.
- Some defense mechanisms against control hijacking attacks are:
  - Stack canaries: A random value (called a canary) is placed on the stack before the return address, and checked before returning from a function. If the canary is corrupted, the program aborts.
  - Address space layout randomization (ASLR): The base addresses of the stack, the heap, and the code segments are randomized at each program execution, making it harder for the attacker to guess the addresses of the target data structures or code.
  - Control-flow integrity (CFI): The program's control-flow graph is statically computed and enforced at runtime, preventing the program from jumping to unexpected locations .