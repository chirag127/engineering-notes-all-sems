## Unit 3 - Secure architecture principles: isolation and least privilege

- Isolation and least privilege are two fundamental principles of secure architecture design that aim to reduce the attack surface and limit the damage of a potential breach.
- Isolation means separating different components or layers of a system, such as data, processes, networks, or users, so that they can only interact through well-defined interfaces and protocols.
- Least privilege means granting the minimum amount of access or permissions to each component or user, based on their legitimate needs and roles, and revoking them when they are no longer needed.
- Some benefits of applying isolation and least privilege are:
  - Reducing the risk of unauthorized access, modification, or disclosure of sensitive data or resources.
  - Containing the impact and spread of malware, ransomware, or other malicious attacks.
  - Enhancing the performance, scalability, and reliability of the system by minimizing dependencies and conflicts.
  - Simplifying the management, monitoring, and auditing of the system by enforcing clear boundaries and responsibilities.
- Some examples of implementing isolation and least privilege are:
  - Using firewalls, virtual private networks (VPNs), or encryption to isolate network segments or communication channels.
  - Applying the principle of defense in depth to layer multiple security controls and mechanisms throughout the system.
  - Using containers, virtual machines, or microservices to isolate applications or processes from each other and from the underlying infrastructure.
  - Adopting the principle of zero trust to verify the identity and context of every request and response, and enforce granular policies based on the principle of least privilege.
  - Applying role-based access control (RBAC) or attribute-based access control (ABAC) to assign permissions and roles to users or groups based on their functions and attributes.
  - Implementing the principle of separation of duties to prevent any single user or component from having too much power or responsibility over the system.
  - Using multifactor authentication (MFA), single sign-on (SSO), or password managers to secure user credentials and access.
  - Following the principle of secure by default to disable or remove any unnecessary or unused features, services, or accounts from the system.