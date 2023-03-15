Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your notes:

### More on confinement techniques

- Confinement techniques are methods to prevent unauthorized information flow from a process or a system to another process or system.
- Confinement techniques aim to enforce the principle of least privilege, which states that a process or a system should only have the minimum access rights necessary to perform its function.
- Confinement techniques can be classified into two categories: static and dynamic.
  - Static confinement techniques are applied before the execution of a process or a system, and they do not change during the execution. Examples of static confinement techniques are access control lists, role-based access control, and mandatory access control.
  - Dynamic confinement techniques are applied during the execution of a process or a system, and they can change according to the context and the behavior of the process or the system. Examples of dynamic confinement techniques are sandboxing, virtualization, and encryption.
- Confinement techniques face the challenge of distinguishing between authorized and unauthorized information flow, especially when the process or the system needs to communicate with other processes or systems. This is known as the confinement problem.
- Confinement techniques also need to consider the possibility of covert channels, which are hidden ways of transmitting information that bypass the normal communication mechanisms. Covert channels can be classified into two types: storage channels and timing channels.
  - Storage channels use a shared resource, such as memory or disk space, to encode and transmit information. For example, a process can write a secret bit to a file and another process can read it later.
  - Timing channels use the timing of events, such as CPU usage or network traffic, to encode and transmit information. For example, a process can vary its execution speed or send packets at different intervals to signal a secret bit to another process.
- Confinement techniques can use various methods to detect, prevent, or limit covert channels, such as monitoring, auditing, noise injection, rate limiting, or randomization. However, covert channels are hard to eliminate completely, and they often require a trade-off between security and performance.