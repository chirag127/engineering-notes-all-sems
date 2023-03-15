# More on confinement techniques

Confinement techniques are methods to prevent unauthorized information flow from a process or a system to another entity. They are based on the principle of least privilege, which states that a process or a system should only have the minimum access rights necessary to perform its function. Confinement techniques can be classified into two categories: static and dynamic.

## Static confinement techniques

Static confinement techniques are applied before or during the execution of a process or a system, and they do not change during the execution. They include:

- Access control mechanisms, such as discretionary access control (DAC), mandatory access control (MAC), or role-based access control (RBAC). These mechanisms enforce rules on who can access what data or resources, and under what conditions. For example, a server application can run as a low-privilege user and have limited read/write/execute permissions on files and directories.
- Encryption mechanisms, such as symmetric encryption, asymmetric encryption, or hybrid encryption. These mechanisms transform data into an unreadable form, and only authorized parties can decrypt it with the proper keys. For example, a process can encrypt its sensitive data before sending it to another process or a network.
- Isolation mechanisms, such as virtualization, sandboxing, or containerization. These mechanisms create separate environments for processes or systems, and limit their interactions with other environments. For example, a process can run in a virtual machine or a sandbox, and have restricted access to the host system or the network.

## Dynamic confinement techniques

Dynamic confinement techniques are applied during the execution of a process or a system, and they can change according to the context or the behavior of the process or system. They include:

- Information flow control mechanisms, such as labels, tags, or taints. These mechanisms mark data or resources with metadata that indicate their confidentiality or integrity level, and track their propagation through the system. For example, a process can label its data with a security level, and prevent it from flowing to a lower-level process or a covert channel.
- Audit mechanisms, such as logs, alerts, or reports. These mechanisms record the activities or events of a process or a system, and detect or report any violations of the security policy. For example, a process can log its actions and data transfers, and alert the administrator if it detects any unauthorized or suspicious information flow.
- Adaptation mechanisms, such as feedback, learning, or self-healing. These mechanisms enable a process or a system to adjust its behavior or configuration based on the feedback from the environment or the user. For example, a process can learn from its past experiences and improve its confinement strategy, or self-heal if it encounters any errors or attacks.

## References

: https://www.geeksforgeeks.org/information-security-confidentiality/

: https://people.cs.rutgers.edu/~pxk/419/notes/confinement.html

: https://www.cisecurity.org/insights/blog/11-cyber-defense-tips-to-stay-secure-at-work-and-home

: https://www.cs.clemson.edu/course/cpsc420/material/Confinement/Problem.pdf