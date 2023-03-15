### Defense against Control Hijacking - Run-time Defenses

- A control hijacking attack exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- A variety of defensive mechanisms have been proposed to mitigate control-flow hijacking attacks. As previously mentioned, complete memory safety, code pointer integrity, and control flow integrity are promising defenses in theory .
- However, these defenses are often impractical or incomplete in practice, due to performance overhead, compatibility issues, or insufficient coverage .
- Therefore, many run-time defenses focus on specific types of control hijacking attacks, such as stack smashing, return-oriented programming, or indirect branch hijacking .
- Some examples of run-time defenses are:

  - Stack canaries: A random value is placed on the stack before the return address, and checked before returning from a function. If the canary is corrupted, the program aborts, preventing the attacker from overwriting the return address .
  - Non-executable memory: The memory regions that store code are marked as executable, and the memory regions that store data are marked as non-executable. This prevents the attacker from injecting and executing malicious code in the data regions .
  - Address space layout randomization (ASLR): The base addresses of the code, data, stack, and heap segments are randomized at program loading or execution time. This makes it harder for the attacker to predict the locations of the code or data they want to hijack .
  - Shadow stacks: A separate stack is maintained to store only the return addresses, and protected from normal memory accesses. This prevents the attacker from tampering with the return addresses on the original stack .
  - Control flow integrity (CFI): A control flow graph (CFG) is constructed at compile time or run time, and used to enforce that the program follows only the valid control flow transitions. This prevents the attacker from diverting the control flow to arbitrary locations .

- These run-time defenses have different strengths and weaknesses, and can be combined to achieve better protection. However, none of them can guarantee complete security, and some of them can be bypassed by advanced attacks   .
- Therefore, it is important to keep improving the existing run-time defenses, and developing new ones, to cope with the evolving threats of control hijacking attacks   .