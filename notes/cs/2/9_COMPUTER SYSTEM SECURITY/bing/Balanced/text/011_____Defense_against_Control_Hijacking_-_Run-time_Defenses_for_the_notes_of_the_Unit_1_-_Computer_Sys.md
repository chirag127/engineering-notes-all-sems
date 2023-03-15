### Defense against Control Hijacking - Run-time Defenses

- A control hijacking attack exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- A variety of defensive mechanisms have been proposed to mitigate control-flow hijacking attacks. As previously mentioned, complete memory safety, code pointer integrity, and control flow integrity are promising defenses in theory .
- However, these defenses are often impractical or incomplete in practice, due to performance overhead, compatibility issues, or insufficient coverage .
- Therefore, some run-time defenses aim to provide partial protection or detection against control hijacking attacks, without enforcing strict memory or control flow policies .
- Some examples of run-time defenses are:
  - Stack canaries: A random value is placed on the stack before the return address, and checked before returning from a function. If the canary is corrupted, the program aborts, preventing a stack-based buffer overflow from overwriting the return address .
  - Non-executable memory: A hardware feature that marks some memory regions as non-executable, preventing the execution of injected code or data .
  - Address space layout randomization (ASLR): A technique that randomizes the base addresses of code, data, stack, and heap segments, making it harder for an attacker to guess the location of a target function or variable .
  - Shadow stacks: A separate stack that stores only return addresses, and is checked against the original stack before returning from a function. This prevents return-oriented programming (ROP) attacks that manipulate the return addresses on the stack .
  - Control flow integrity (CFI): A technique that restricts the possible targets of indirect control transfers (such as function pointers or return addresses) to a precomputed set of valid destinations, based on a control flow graph (CFG) of the program .