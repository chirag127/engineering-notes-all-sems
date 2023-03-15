### Advanced Control Hijacking Attacks

- A control hijacking attack is carried out by overwriting part of the data structures of a victim program, causing it to lose control of its control flow and, as a result, the program's and perhaps the underlying system's control .
- Control hijacking attacks can be classified into two categories: direct and indirect.
  - Direct control hijacking attacks involve overwriting a function return address or a function pointer with the address of malicious code, such as a shellcode or a gadget.
  - Indirect control hijacking attacks involve manipulating the data used by indirect branches, such as virtual function tables, jump tables, or global offset tables.
- Some examples of advanced control hijacking attacks are:
  - Return-oriented programming (ROP): a technique that chains together short sequences of instructions (gadgets) that end with a return instruction, to execute arbitrary code without injecting any code.
  - Jump-oriented programming (JOP): a technique that uses a dispatcher gadget to execute other gadgets that end with an indirect jump instruction, to bypass defenses that prevent return instructions from being overwritten.
  - Data-oriented programming (DOP): a technique that modifies the data used by the program logic, such as flags, counters, or pointers, to alter the program behavior without changing the control flow.
- Some defenses against control hijacking attacks are:
  - Stack canaries: a random value placed on the stack before the return address, to detect stack buffer overflows before the return address is overwritten.
  - Non-executable memory: a mechanism that prevents the execution of code from memory regions that are marked as non-executable, such as the stack or the heap.
  - Address space layout randomization (ASLR): a mechanism that randomizes the base addresses of the code, data, stack, and heap segments, to make it harder for the attacker to guess the addresses of the target code or data.
  - Control-flow integrity (CFI): a mechanism that enforces the intended control flow of the program, by checking the validity of the target address of each indirect branch.