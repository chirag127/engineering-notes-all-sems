### Advanced Control Hijacking Attacks

- A control hijacking attack is a type of network security attack in which the attacker takes control of the execution flow of a victim program or system by altering some data structures that affect the control flow  .
- The attacker can exploit vulnerabilities such as buffer overflows, format string bugs, or heap corruption to overwrite code pointers (values that influence the program counter or instruction pointer) or data values that are used to determine the control flow .
- The attacker can then execute arbitrary code (code injection attacks) or reuse existing code (code reuse attacks) to achieve malicious goals such as stealing information, escalating privileges, or compromising the system .
- Some examples of control hijacking attacks are:
  - Return-to-libc attack: The attacker overwrites the return address of a function with the address of a library function (such as system) and passes malicious arguments to execute arbitrary commands.
  - Return-oriented programming (ROP) attack: The attacker chains together short sequences of instructions (called gadgets) that end with a return instruction, and overwrites the return address of a function with the address of the first gadget. The gadgets can perform various operations such as loading registers, performing arithmetic, or calling system calls.
  - Jump-oriented programming (JOP) attack: The attacker uses a dispatcher gadget that can jump to different gadgets based on a register value, and overwrites a code pointer with the address of the dispatcher. The gadgets can perform similar operations as in ROP, but without using return instructions.
- Some defensive mechanisms against control hijacking attacks are:
  - Stack canaries: A random value is placed between the local variables and the return address of a function, and checked before returning. If the canary is corrupted, the program aborts.
  - Non-executable memory: The memory regions that contain data (such as stack and heap) are marked as non-executable, so that the attacker cannot inject and execute code there.
  - Address space layout randomization (ASLR): The memory regions that contain code (such as libraries and executable) are loaded at random addresses, so that the attacker cannot predict the addresses of code pointers or gadgets.
  - Control-flow integrity (CFI): The program's control-flow graph is analyzed and enforced at runtime, so that the attacker cannot divert the control flow to unexpected locations.