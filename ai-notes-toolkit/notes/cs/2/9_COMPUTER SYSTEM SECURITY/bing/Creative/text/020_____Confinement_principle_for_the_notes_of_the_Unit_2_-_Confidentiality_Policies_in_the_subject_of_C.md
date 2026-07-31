### Confinement principle

- The confinement principle is a security principle that says that a server shouldn't give out information that the user of the service thinks is private.
- The confinement principle stops a process from doing things that are not allowed, such as leaking confidential data, corrupting other processes, or consuming excessive resources .
- Confinement is a mechanism for enforcing the principle of least privilege, which means that a process should only have the minimum permissions and resources necessary to perform its function.
- The problem of confinement is that the confined process may need to transmit data to another process, and the confinement mechanism must distinguish between transmission of authorized data and transmission of unauthorized data.
- This presents a dilemma in that modern computers are designed to share resources and yet by the act of sharing they create channels of communication along which information can be leaked.
- Confinement can be implemented at different levels, such as threads, applications, processes, or virtual machines.
- Some examples of confinement techniques are software fault isolation, sandboxing, firewalls, encryption, and access control .