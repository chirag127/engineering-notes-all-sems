### Confinement Principle

The confinement principle is a mechanism for enforcing the principle of least privilege. It is a part of the core security principles of Confidentiality, Integrity, and Availability. The confinement principle says that a server shouldn't give out information that the user of the service thinks is private. The confinement principle stops a process from doing things that are not allowed.

In confinement principle, access control affects the server in two ways:

1. The goal of the service provider: The server must ensure that the resources that are being accessed on the behalf of the client include only those resources that the client is authorized for.
2. The goal of the service user: The server must ensure the privacy of the service user.

The problem is that the confined process needs to transmit data to another process. The confinement mechanism must distinguish between transmission of authorized data and the transmission of unauthorized data.