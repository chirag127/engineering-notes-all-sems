### Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or data into the program's memory and manipulate the program counter or return address to execute the injected code or data.
- The goal of control hijacking is to gain unauthorized access, privilege escalation, data theft, denial of service, or other malicious actions on the target system.
- Some common types of control hijacking attacks are:
  - Buffer overflow attacks: The attacker overwrites the buffer boundaries and corrupts the adjacent memory locations, such as the return address or the stack frame pointer. The attacker can then redirect the execution to the injected code or data, or to a different location in the program.
  - Integer overflow attacks: The attacker exploits an arithmetic operation that results in a value that is too large or too small to be stored in the variable type, causing a wraparound or truncation. The attacker can then use the corrupted value to bypass security checks, access out-of-bounds memory, or cause unexpected behavior.
  - Format string attacks: The attacker exploits a format string vulnerability, which occurs when a user-supplied input is passed as a format string argument to a function like printf. The attacker can then use format specifiers to read or write arbitrary memory locations, or to execute arbitrary code.
- Some common defenses against control hijacking attacks are:
  - Input validation: The program checks the length, type, and format of the user input and rejects any invalid or malicious input. This can prevent the attacker from injecting code or data into the program's memory.
  - Ciphering: The program encrypts the data or packets that are transmitted over the network, so that the attacker cannot decipher or tamper with them. This can prevent the attacker from intercepting or spoofing the communication.
  - Runtime checking: The program uses techniques like stack canaries, address space layout randomization, or control flow integrity to detect or prevent any modification of the control flow data or the program layout. This can prevent the attacker from redirecting the execution to the injected code or data, or to a different location in the program.