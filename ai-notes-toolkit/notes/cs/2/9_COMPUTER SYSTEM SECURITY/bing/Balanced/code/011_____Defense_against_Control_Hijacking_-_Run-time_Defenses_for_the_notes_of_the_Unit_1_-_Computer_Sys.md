Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Defense against Control Hijacking - Run-time Defenses for the Unit 1 - Computer System Security Introduction in the subject of COMPUTER SYSTEM SECURITY.

### Defense against Control Hijacking - Run-time Defenses

- A control hijacking attack exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- A variety of defensive mechanisms have been proposed to mitigate control-flow hijacking attacks. As previously mentioned, complete memory safety, code pointer integrity, and control flow integrity are promising defenses in theory.
- However, in practice, these defenses are often too expensive, too imprecise, or too incompatible with existing software and hardware to be widely adopted.
- Therefore, many run-time defenses focus on specific types of control hijacking attacks, such as stack smashing, return-oriented programming, or code injection, and try to prevent or detect them with lower overhead, higher accuracy, or better compatibility.
- Some examples of run-time defenses are:

  - Stack canaries: A random value is placed on the stack before the return address, and checked before returning from a function. If the canary is corrupted, it indicates a buffer overflow attack and the program is terminated.
  - Non-executable memory: A hardware or software mechanism that marks certain memory regions as non-executable, preventing code injection attacks that try to execute malicious code stored in data segments.
  - Address space layout randomization (ASLR): A technique that randomizes the base addresses of code and data segments, making it harder for attackers to guess the locations of code pointers or gadgets.
  - Shadow stacks: A separate stack that stores only return addresses, and is checked against the original stack before returning from a function. This prevents attacks that overwrite return addresses with arbitrary values.
  - Control flow integrity (CFI): A technique that enforces that the control flow of a program follows a precomputed control flow graph (CFG), which represents all the valid transitions between basic blocks. This prevents attacks that divert the control flow to arbitrary locations.

- These run-time defenses have different strengths and weaknesses, and can be combined to achieve better protection. However, none of them can guarantee complete security, and some of them can be bypassed by advanced attacks that exploit their limitations or assumptions.
- Therefore, it is important to keep improving the design and implementation of run-time defenses, as well as developing new techniques that can address the challenges of modern software and hardware systems.