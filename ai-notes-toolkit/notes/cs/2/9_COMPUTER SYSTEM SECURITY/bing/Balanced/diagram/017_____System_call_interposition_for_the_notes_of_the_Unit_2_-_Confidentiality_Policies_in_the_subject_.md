### System call interposition

- System call interposition (SCI) is a method for monitoring and regulating the behavior of applications by intercepting their calls to system functions    .
- System functions are the interfaces between the user space and the kernel space, and they provide access to various resources and services, such as files, sockets, processes, signals, etc.
- By replacing the original system functions with interposed functions, SCI can enforce a security policy that either approves or rejects the call based on the arguments and the context of the caller   .
- SCI can be implemented in different ways, such as using dynamic linking, binary rewriting, library preloading, kernel modules, or virtual machine monitors  .
- SCI can be used for various security purposes, such as sandboxing, intrusion detection, auditing, logging, debugging, etc   .
- SCI also faces some challenges and limitations, such as performance overhead, transparency, completeness, correctness, and robustness   .
- SCI requires a careful design and implementation to avoid traps and pitfalls that can compromise its effectiveness and security .