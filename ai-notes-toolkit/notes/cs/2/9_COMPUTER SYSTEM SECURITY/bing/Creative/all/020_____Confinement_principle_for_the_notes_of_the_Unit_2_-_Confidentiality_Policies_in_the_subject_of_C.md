# Confinement Principle

- The confinement principle is a security principle that says that a server shouldn't give out information that the user of the service thinks is private.
- The confinement principle stops a process from doing things that are not allowed, such as leaking sensitive data, modifying system files, or launching attacks on other processes.
- Confinement is a mechanism for enforcing the principle of least privilege, which means that a process should only have the minimum permissions and resources necessary to perform its function.
- The problem is that the confined process may need to transmit data to another process, and the confinement mechanism must distinguish between transmission of authorized data and the transmission of unauthorized data.
- This presents a dilemma in that modern computers are designed to share resources and yet by the act of sharing they create channels of communication along which information can be leaked.
- Confinement can be implemented at different levels, such as threads, applications, processes, or virtual machines .
- Some examples of confinement techniques are:
  - Software Fault Isolation (SFI): a technique that isolates threads sharing the same address space by using memory protection and code verification.
  - Browser-based confinement: a technique that restricts the access of web applications to the browser's sandbox and the same-origin policy.
  - Virtual Machine (VM) subversion: a technique that runs untrusted code in a separate VM that can be monitored and controlled by the host system.