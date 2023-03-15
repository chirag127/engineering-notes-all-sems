### Advanced Control Hijacking Attacks

- A control hijacking attack is carried out by overwriting part of the data structures of a victim program, causing it to lose control of its control flow and, as a result, the program's and perhaps the underlying system's control .
- A control hijacking attack exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- Control-hijacking attacks are also known as control-flow hijacking attacks.
- Some examples of control hijacking attacks are:
  - Buffer overflow attacks: The attacker overwrites the return address or a function pointer on the stack or the heap with a malicious address that points to the attacker's code.
  - Return-oriented programming (ROP) attacks: The attacker chains together short sequences of instructions (called gadgets) that end with a return instruction, and overwrites the return address on the stack with the address of the first gadget.
  - Jump-oriented programming (JOP) attacks: The attacker uses a dispatcher gadget that reads the address of the next gadget from a data structure (called a jump table), and overwrites a function pointer or a register with the address of the dispatcher gadget.
  - Remote desktop protocol (RDP) hijacking attacks: The attacker logs into a remote server and uses commands to take over the sessions of other connected users, gaining access to their desktops and applications.
- Some defense mechanisms against control hijacking attacks are:
  - Stack canaries: A random value is placed on the stack before the return address, and checked before returning from a function. If the canary is corrupted, the program aborts.
  - Non-executable memory: The memory regions that contain data (such as the stack and the heap) are marked as non-executable, preventing the attacker from executing code from those regions.
  - Address space layout randomization (ASLR): The memory regions that contain code (such as the text segment and the libraries) are randomly placed in the address space, making it harder for the attacker to guess the addresses of the gadgets.
  - Control-flow integrity (CFI): The program's control-flow graph is statically analyzed, and runtime checks are inserted to ensure that the control flow follows the legitimate paths.
  - Authentication and encryption: The RDP sessions are secured with strong authentication and encryption protocols, preventing the attacker from intercepting or hijacking the sessions.