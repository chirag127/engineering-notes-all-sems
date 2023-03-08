### Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or data into the program's memory and manipulate the program counter or return address to execute the injected code or data.
- The goal of control hijacking is to gain unauthorized access, privilege escalation, data theft, denial of service, or other malicious actions on the target system or network.
- Control hijacking can be classified into two categories: code injection attacks and code reuse attacks.
  - Code injection attacks involve injecting new code into the program's memory and redirecting the control flow to execute it. Examples of code injection attacks are buffer overflow, heap overflow, format string, and shellcode attacks.
  - Code reuse attacks involve reusing existing code in the program's memory and redirecting the control flow to execute it in a different order or context. Examples of code reuse attacks are return-oriented programming (ROP), jump-oriented programming (JOP), and return-to-libc attacks.
- Control hijacking can be prevented or mitigated by various techniques, such as:
  - Input validation and sanitization to avoid memory corruption vulnerabilities.
  - Memory protection mechanisms, such as non-executable memory, stack canaries, address space layout randomization (ASLR), and control flow integrity (CFI) to prevent or detect unauthorized code execution or modification.
  - Cryptographic techniques, such as encryption, authentication, and integrity checking to protect the communication channels and data from hijacking.
  - Session management techniques, such as session tokens, timeouts, and logout to prevent session hijacking attacks.
  - Code obfuscation and diversification to make the program code harder to analyze and reuse by the attacker.

Some possible mnemonics and learning tricks for the topic are:

- To remember the types of code injection attacks, use the acronym BFSH: Buffer overflow, Format string, Shellcode, Heap overflow.
- To remember the types of code reuse attacks, use the acronym RJR: Return-oriented programming, Jump-oriented programming, Return-to-libc.
- To remember the memory protection mechanisms, use the acronym SNAC: Stack canaries, Non-executable memory, ASLR, CFI.
- To remember the session management techniques, use the acronym STOL: Session tokens, Timeouts, Logout.
- To remember the difference between code injection and code reuse attacks, use the analogy of a book: Code injection is like writing a new chapter in the book and making the reader read it, while code reuse is like rearranging the existing chapters in the book and making the reader read them in a different order.