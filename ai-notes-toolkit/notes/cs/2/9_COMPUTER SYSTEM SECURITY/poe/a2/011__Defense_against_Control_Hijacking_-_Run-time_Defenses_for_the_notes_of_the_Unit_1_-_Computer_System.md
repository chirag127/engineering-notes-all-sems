 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Defense against Control Hijacking - Run-time Defenses

- Validate Inputs: Validate all inputs before processing them. This defends against buffer overflow attacks that provide malicious input to gain control.
- Use non-executable stacks and heaps: Make stack and heap non-executable so that malicious code cannot be executed from there even if the buffer overflow succeeds. This makes code injection attacks ineffective.
- Address space layout randomization: Randomize the base address of key data areas like stack, heap, etc. so that attackers cannot reliably jump to a known address location to execute their code. This makes exploitation of memory corruption vulnerabilities more difficult.
- Data execution prevention: Mark memory regions as non-executable unless they are explicitly marked as executable. This prevents execution of code from data areas and reduces the threat of code injection attacks.
- Disable risky functions: Disable functions like "gets()" that can lead to vulnerabilities if misused. Force the use of safe alternatives like "fgets()".
- Sandboxing: Run programs with limited privileges in sandboxed environments to limit the damage caused by successful exploitations. The sandbox prevents access to critical resources.
- Diversity: Employ diverse and obfuscated ways for implementations to complicate reverse engineering attempts and make attacks more difficult. Diverse implementations reduce the applicability of general attacks.

The above points cover some key run-time defenses that can be employed to counter control hijacking attacks by making exploitation of vulnerabilities more difficult and limiting the damage caused by any successful exploits. A combination of multiple defenses is typically used to provide stronger security.