# Defense against Control Hijacking - Platform Defenses

Control hijacking is a type of attack that exploits a vulnerability in a program to alter its execution flow and execute malicious code. Control hijacking can be performed by overwriting code pointers, such as return addresses, function pointers, or exception handlers, with the address of the attacker's payload. The payload can be injected into the program's memory or stored in an existing location, such as the stack, the heap, or the data segment.

To defend against control hijacking, several platform defenses have been proposed, such as:

- **Fixing bugs**: The most obvious and effective way to prevent control hijacking is to eliminate the vulnerabilities that allow it in the first place. This can be done by auditing the software, using automated tools, such as Coverity or Prefast/Prefix, or rewriting the software in a type-safe language, such as Java or ML. However, this is difficult for existing (legacy) code, and may not be feasible for all applications or platforms.

- **Stack protection**: A common technique to protect the return addresses on the stack is to use a canary, a random value that is placed between the return address and the local variables. The canary is checked before returning from a function, and if it is modified, the program aborts. This can prevent simple buffer overflow attacks, but not more sophisticated ones that can bypass or guess the canary. Examples of stack protection mechanisms are StackGuard, ProPolice, and StackShield.

- **Non-executable memory**: Another technique to prevent control hijacking is to mark the memory regions that contain data as non-executable, so that the processor will not execute any code from them. This can prevent code injection attacks, but not return-to-libc or return-oriented programming attacks, which use existing code in the program or the libraries. Examples of non-executable memory mechanisms are NX bit, DEP, and W^X.

- **Address space layout randomization (ASLR)**: A technique to make control hijacking harder is to randomize the layout of the program's address space, such as the base addresses of the code, the stack, the heap, and the libraries. This can make it difficult for the attacker to predict the location of the payload or the existing code. However, ASLR can be defeated by information leakage, brute force, or partial overwrite attacks. Examples of ASLR mechanisms are PaX, ASLR, and PIE.

- **Control flow integrity (CFI)**: A technique to enforce the intended control flow of the program is to use a control flow graph (CFG), which represents the valid transitions between basic blocks of code. The CFG can be constructed statically or dynamically, and can be enforced at compile time, link time, or run time. CFI can prevent arbitrary control flow redirection, but not attacks that follow the CFG. Examples of CFI mechanisms are CFI, BinCFI, and ROPecker .

- **Code pointer integrity (CPI)**: A technique to protect the integrity of the code pointers is to isolate them from the data memory, and use a separate memory region, called the safe region, to store them. The safe region can be protected by hardware or software mechanisms, and can be accessed only by authorized instructions. CPI can prevent code pointer corruption, but not attacks that exploit existing code pointers. Examples of CPI mechanisms are CPI, CCFI, and CPI^2^.

: https://citizenchoice.in/course/Computer-System-Security/Chapter%201%20:%20Introduction/Control-Hijacking-Run-time-Defenses-1
: https://www.scribd.com/presentation/347261651/Module-1-4-pptx
: https://dspace.mit.edu/bitstream/handle/1721.1/106003/965799420-MIT.pdf?sequence=1
: http://web.mit.edu/ha22286/www/papers/MEng15_2.pdf