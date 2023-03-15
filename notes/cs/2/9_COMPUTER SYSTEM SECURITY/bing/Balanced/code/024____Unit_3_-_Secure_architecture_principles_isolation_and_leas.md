## Unit 3 - Secure architecture principles: isolation and least privilege

- Isolation and least privilege are two fundamental principles of secure architecture design that aim to reduce the attack surface and limit the damage of a potential breach.
- Isolation refers to the separation of different components or layers of a system, such as data, processes, networks, or users, so that they cannot interfere with each other or access unauthorized resources.
- Least privilege refers to the restriction of the permissions or capabilities of a component or a user to the minimum necessary to perform its function, such as read, write, execute, or communicate.
- Some benefits of applying isolation and least privilege are:
  - Reduced risk of unauthorized access, modification, or disclosure of sensitive data or resources.
  - Reduced risk of propagation or escalation of attacks across the system or network.
  - Reduced risk of accidental or intentional misuse or abuse of privileges or resources by users or components.
  - Improved performance, reliability, and availability of the system or network by minimizing dependencies and conflicts.
- Some examples of applying isolation and least privilege are:
  - Using firewalls, routers, or virtual private networks (VPNs) to isolate different segments or zones of a network, such as public, private, or demilitarized zones (DMZs), and enforce access control policies based on the principle of least privilege.
  - Using encryption, hashing, or digital signatures to isolate and protect data in transit or at rest from unauthorized access or tampering.
  - Using containers, virtual machines, or sandboxes to isolate and run applications or processes in isolated environments that limit their access to system resources or other applications or processes.
  - Using role-based access control (RBAC), discretionary access control (DAC), or mandatory access control (MAC) to assign and enforce the least privilege permissions or capabilities for users or components based on their roles, identities, or security labels.