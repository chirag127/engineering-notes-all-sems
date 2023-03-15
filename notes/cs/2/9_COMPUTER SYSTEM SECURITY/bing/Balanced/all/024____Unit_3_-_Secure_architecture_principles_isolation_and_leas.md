## Unit 3 - Secure architecture principles: isolation and least privilege

- Isolation and least privilege are two fundamental principles of secure architecture design that aim to reduce the attack surface and limit the damage of a potential breach.
- Isolation means separating different components or layers of a system, such as data, processes, networks, or users, so that they can only interact through well-defined interfaces and protocols.
- Least privilege means granting the minimum amount of access or permissions to each component or user, based on the principle of need-to-know and need-to-do.
- Some benefits of applying isolation and least privilege are:
  - Reduced risk of unauthorized access, modification, or disclosure of sensitive data or resources.
  - Reduced risk of propagation or escalation of attacks across the system or network.
  - Reduced complexity and increased modularity of the system, which facilitates maintenance, testing, and auditing.
  - Increased performance and availability of the system, as failures or errors are contained and isolated.
- Some examples of applying isolation and least privilege are:
  - Using firewalls, routers, or virtual private networks (VPNs) to isolate different network segments or zones, such as public, private, or demilitarized zones (DMZs).
  - Using encryption, authentication, or access control mechanisms to protect data in transit or at rest, and to enforce the principle of least privilege for data access.
  - Using containers, virtual machines, or microservices to isolate different processes or applications, and to limit their resource consumption and communication channels.
  - Using role-based access control (RBAC), multi-factor authentication (MFA), or password policies to restrict user access and privileges, and to enforce the principle of least privilege for user actions.