# Defense against Control Hijacking - Platform Defenses

## Introduction
Control hijacking is a type of attack where an attacker takes control of the flow of a program. This can be done by exploiting vulnerabilities in the software, such as buffer overflows or format string vulnerabilities. To defend against control hijacking, a variety of defensive mechanisms have been proposed.

## Platform Defenses
1. **Fixing Bugs**: One way to prevent control hijacking attacks is to fix the bugs in the software that allow the attack to occur. This can be done through auditing the software and using automated tools such as Coverity or Prefast/Prefix. Rewriting the software in a type-safe language such as Java or ML can also help prevent control hijacking attacks, although this can be difficult for existing (legacy) code.

2. **Complete Memory Safety**: Complete memory safety is a promising defense against control hijacking attacks. This means ensuring that all memory accesses are within the bounds of the allocated memory and that memory is not accessed after it has been freed.

3. **Code Pointer Integrity**: Code pointer integrity is another promising defense against control hijacking attacks. This means ensuring that all code pointers (such as function pointers or return addresses) are not modified by an attacker.

4. **Control Flow Integrity**: Control flow integrity (CFI) is a security policy that dictates that any execution of a program must follow a path of a Control Flow Graph (CFG) determined ahead of time. In its ideal form, CFI is a promising enforcement mechanism against attacks that arbitrarily control and hijack a program's behavior.

## Conclusion
In conclusion, there are several platform defenses that can be used to defend against control hijacking attacks. These include fixing bugs, ensuring complete memory safety, maintaining code pointer integrity, and enforcing control flow integrity. These defenses can help prevent attackers from taking control of the flow of a program and executing malicious code.