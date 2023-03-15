# Advanced Control Hijacking Attacks

- A control hijacking attack is a type of network security attack in which the attacker takes control of the execution flow of a victim program or system by exploiting a vulnerability, such as a buffer overflow .
- The attacker can overwrite some data structures in the victim program that affect its control flow, such as return addresses, function pointers, or exception handlers .
- The attacker can then redirect the execution flow to a malicious code segment, either injected by the attacker or already existing in the program or system .
- Some examples of control hijacking attacks are code injection attacks, code reuse attacks, return-oriented programming, and jump-oriented programming  .
- Control hijacking attacks can compromise the confidentiality, integrity, and availability of the victim program or system, and potentially allow the attacker to execute arbitrary commands or gain unauthorized access to resources .
- Some defensive mechanisms against control hijacking attacks are stack canaries, address space layout randomization, non-executable memory, control-flow integrity, and code signing  .