Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Defense against Control Hijacking - Run-time Defenses for the Unit 1 - Computer System Security Introduction in the subject of COMPUTER SYSTEM SECURITY.

### Defense against Control Hijacking - Run-time Defenses

- A control hijacking attack exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- A variety of defensive mechanisms have been proposed to mitigate control-flow hijacking attacks. As previously mentioned, complete memory safety, code pointer integrity, and control flow integrity are promising defenses in theory.
- However, these defenses are often impractical or incomplete in practice, due to performance overhead, compatibility issues, or insufficient coverage.
- Therefore, many run-time defenses focus on specific types of control hijacking attacks, such as stack smashing, return-oriented programming, or code injection.
- Some examples of run-time defenses are:

  - Stack canaries: A random value is placed on the stack before the return address, and checked before returning from a function. If the canary is corrupted, the program aborts, preventing the attacker from overwriting the return address.
  - Address space layout randomization (ASLR): The base addresses of the stack, heap, libraries, and executable are randomized at load time, making it harder for the attacker to predict the location of code or data.
  - Non-executable memory (NX): The memory pages that contain data are marked as non-executable, preventing the attacker from injecting and executing arbitrary code on the stack or heap.
  - Control flow integrity (CFI): The program's control flow graph (CFG) is determined ahead of time, and enforced at run time by checking the validity of indirect branches and returns. If the control flow deviates from the CFG, the program aborts, preventing the attacker from redirecting the execution to arbitrary locations.
  - Shadow stacks: A separate stack is maintained for storing return addresses, and checked before returning from a function. If the return address on the shadow stack does not match the one on the regular stack, the program aborts, preventing the attacker from overwriting the return address.
  - Code pointer hiding: The code pointers (such as return addresses, function pointers, or vtable pointers) are encrypted or obfuscated, and only decrypted or deobfuscated when needed. This makes it harder for the attacker to locate and tamper with the code pointers.

- These run-time defenses have different strengths and weaknesses, such as performance overhead, security guarantees, compatibility, and usability.
- Some of these defenses can be combined or enhanced to provide stronger protection against control hijacking attacks.
- However, none of these defenses are perfect, and some of them can be bypassed or weakened by advanced attacks, such as information leaks, code reuse, or memory disclosure.
- Therefore, it is important to evaluate the effectiveness and limitations of these run-time defenses, and to design new defenses that can cope with the evolving threat landscape.