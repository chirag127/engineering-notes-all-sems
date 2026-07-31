### Advanced Control Hijacking Attacks

- A control hijacking attack is carried out by overwriting part of the data structures of a victim program, causing it to lose control of its control flow and, as a result, the program's and perhaps the underlying system's control .
- Control hijacking attacks can be classified into two categories: direct and indirect.
  - Direct control hijacking attacks involve overwriting a function return address, a function pointer, or a longjmp buffer with the address of malicious code.
  - Indirect control hijacking attacks involve manipulating the data or metadata used by indirect branches, such as virtual function tables, switch tables, or global offset tables.
- Some examples of advanced control hijacking attacks are:
  - Return-oriented programming (ROP): a technique that exploits a stack buffer overflow to execute a sequence of instructions that are already present in the executable memory of the victim program.
  - Jump-oriented programming (JOP): a technique that exploits a heap buffer overflow to execute a sequence of instructions that are controlled by a dispatcher gadget, which is a piece of code that reads the next instruction address from a data structure.
  - RDP hijacking: a technique that exploits the Remote Desktop Protocol (RDP) to take over an active session of another user and execute commands on their behalf.
- Some possible defenses against control hijacking attacks are:
  - Stack canaries: a random value that is placed between the local variables and the return address on the stack, and is checked before returning from a function to detect any stack corruption.
  - Non-executable memory: a mechanism that prevents the execution of code from memory regions that are marked as data, such as the stack or the heap.
  - Control-flow integrity (CFI): a mechanism that enforces the intended control flow of a program by checking the validity of indirect branches at runtime.