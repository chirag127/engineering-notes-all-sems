### Control Hijacking

- Control hijacking is a type of attack that exploits a program error, particularly a memory corruption vulnerability, at runtime to subvert the intended control flow of a program.
- The attacker can inject malicious code or redirect the execution to existing code in the program or the system libraries.
- The goal of control hijacking is to execute arbitrary code or commands on the target system, such as stealing sensitive data, installing malware, or compromising other systems.
- Some common types of control hijacking attacks are:
  - Buffer overflow attacks: The attacker overwrites the memory beyond the allocated space of a buffer, which may contain return addresses, function pointers, or other control data.
  - Integer overflow attacks: The attacker exploits an arithmetic operation that results in a value that is too large or too small to be stored in the variable, which may lead to memory corruption or incorrect branching.
  - Format string attacks: The attacker exploits a format string vulnerability, which allows the attacker to read or write arbitrary memory locations by supplying specially crafted format specifiers.
  - Session hijacking attacks: The attacker intercepts or cracks the session tokens that are used to authenticate the user on a web server, and gains unauthorized access to the user's online account or profile .
- Some possible defenses against control hijacking attacks are:
  - Ciphering the packets: This prevents the attacker from deciphering the packet headers and obtaining any information that can aid in spoofing or hijacking the network session.
  - Updating the operating system and the software: This reduces the chances of exploiting known vulnerabilities that may have been patched by the vendors.
  - Increasing the browser security settings: This restricts the execution of scripts or plugins that may contain malicious code or exploit browser vulnerabilities.
  - Avoiding questionable websites and downloads: This reduces the exposure to malicious content or software that may compromise the system.
  - Using runtime checking tools: This detects and prevents buffer overflows, integer overflows, or format string vulnerabilities by adding checks or protections to the program code or the memory layout .