### Defense against Control Hijacking - Run-time Defenses

- A control hijacking attack exploits a program error, particularly a memory corruption vulnerability, at application runtime to subvert the intended control flow of a program.
- A variety of defensive mechanisms have been proposed to mitigate control-flow hijacking attacks.
- Complete memory safety, code pointer integrity, and control flow integrity are promising defenses in theory.
- Control Flow Integrity (CFI) is a promising enforcement mechanism against attacks that arbitrarily control and hijack a program's behavior in general.
- The CFI security policy dictates that any execution of a program must follow a path of a Control Flow Graph (CFG) determined ahead of time.