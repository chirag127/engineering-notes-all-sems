### Confinement Principle

- The confinement principle states that a server should not give out information that the user of the service thinks is private.
- The confinement principle stops a process from doing things that are not allowed.
- Confinement is a mechanism for enforcing the principle of least privilege.
- The problem is that the confined process needs to transmit data to another process.
- The confinement mechanism must distinguish between transmission of authorized data and the transmission of unauthorized data.
- In confinement principle, access control affects the server in two ways:
    - The goal of the service provider: The server must ensure that the resources that are being accessed on behalf of the client include only those resources that the client is authorized for.
    - The goal of the service user: The server must ensure the privacy of the service user.