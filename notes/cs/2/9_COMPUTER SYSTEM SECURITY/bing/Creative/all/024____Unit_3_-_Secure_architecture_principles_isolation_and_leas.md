# Unit 3 - Secure architecture principles: isolation and least privilege

- Isolation and least privilege are two important principles of secure design that aim to reduce the attack surface and limit the damage of a potential breach.
- Isolation means separating different components or layers of a system, such as data, processes, networks, or users, so that they cannot interfere with each other or access unauthorized resources.
- Least privilege means granting only the minimum permissions or access rights needed for a component or user to perform a specific task or function, and revoking them when they are no longer needed.
- Some benefits of applying isolation and least privilege are:
  - Improved confidentiality, integrity, and availability of data and resources.
  - Reduced risk of unauthorized access, modification, or deletion of data or resources.
  - Reduced risk of lateral movement, privilege escalation, or data exfiltration by attackers.
  - Easier auditing, monitoring, and logging of activities and events.
  - Easier troubleshooting, testing, and maintenance of the system.
- Some examples of implementing isolation and least privilege are:
  - Using separate servers, virtual machines, containers, or microservices for different applications or functions, and restricting network communication between them using firewalls, network security groups, or service meshes.
  - Using encryption, hashing, or digital signatures to protect data at rest and in transit, and using secure protocols, such as HTTPS, TLS, or SSH, to communicate with external systems or users.
  - Using role-based access control (RBAC), identity and access management (IAM), or multi-factor authentication (MFA) to assign and verify the identity and permissions of users or components, and using the principle of least privilege to grant only the necessary access rights for each role or identity.
  - Using sandboxing, virtualization, or containerization to isolate untrusted or potentially malicious code or processes from the rest of the system, and limiting their access to system resources, such as memory, CPU, disk, or network.
  - Using code signing, code analysis, or code review to ensure the quality and security of the code, and using secure coding practices, such as input validation, output encoding, or error handling, to prevent common vulnerabilities, such as buffer overflow, SQL injection, or cross-site scripting.