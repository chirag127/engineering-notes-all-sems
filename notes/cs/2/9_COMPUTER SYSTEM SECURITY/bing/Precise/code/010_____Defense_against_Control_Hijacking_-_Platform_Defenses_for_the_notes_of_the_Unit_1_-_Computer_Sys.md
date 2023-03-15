### Defense against Control Hijacking - Platform Defenses

1. A variety of defensive mechanisms have been proposed to mitigate control-flow hijacking attacks. Complete memory safety, code pointer integrity, and control flow integrity are promising defenses in theory.
2. One way to prevent hijacking attacks is to fix bugs in the software. This can be done through auditing the software and using automated tools such as Coverity and Prefast/Prefix.
3. Another way to prevent hijacking attacks is to rewrite the software in a type-safe language such as Java or ML. However, this can be difficult for existing (legacy) code.
4. Control Flow Integrity (CFI) is a promising enforcement mechanism against attacks that arbitrarily control and hijack a program's behavior in general. The CFI security policy dictates that any execution of a program must follow a path of a Control Flow Graph (CFG) determined ahead of time.