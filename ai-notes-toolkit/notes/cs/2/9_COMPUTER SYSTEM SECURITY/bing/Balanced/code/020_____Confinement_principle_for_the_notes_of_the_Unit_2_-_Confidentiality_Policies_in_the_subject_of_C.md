### Confinement principle

- The confinement principle says that a server shouldn't give out information that the user of the service thinks is private.
- The confinement principle stops a process from doing things that are not allowed.
- Confinement is a mechanism for enforcing the principle of least privilege.
- The problem is that the confined process needs to transmit data to another process.
- The confinement needs to be on the transmission, not on the data access.
- The confinement mechanism must distinguish between transmission of authorized data and the transmission of unauthorized data.
- This presents a dilemma in that modern computers are designed to share resources and yet by the act of sharing they create channels of communications along which information can be leaked.
- Confinement can be implemented at many levels, such as threads, applications, virtual machines, etc .
- Confinement can be achieved by various techniques, such as encryption, sandboxing, isolation, etc .
- Confinement can prevent or mitigate attacks such as information leakage, code injection, privilege escalation, etc .