## Unit 3 - Secure architecture principles: isolation and least privilege

- Secure architecture principles are guidelines for designing systems that are resilient to threats and attacks.
- Isolation and least privilege are two important principles of secure architecture that aim to limit the exposure and impact of potential vulnerabilities.
- Isolation means separating different components or layers of a system, such as data, processes, networks, or users, so that they cannot interfere with each other or access unauthorized resources.
- Least privilege means granting the minimum level of access or permissions required for a component or user to perform a specific task or function, and revoking them when they are no longer needed.
- Some benefits of applying isolation and least privilege are:
  - Reducing the attack surface and the risk of lateral movement or escalation of privileges by malicious actors.
  - Enhancing the confidentiality, integrity, and availability of data and resources by preventing unauthorized access or modification.
  - Simplifying the management and auditing of security policies and controls by enforcing the principle of separation of duties and roles.
  - Improving the performance and scalability of the system by minimizing the dependencies and interactions between components.
- Some examples of implementing isolation and least privilege are:
  - Using virtualization, containers, or microservices to isolate applications or services from each other and from the underlying infrastructure.
  - Applying network segmentation, firewalls, or encryption to isolate different network zones or domains and protect data in transit.
  - Implementing authentication, authorization, and encryption to isolate different users or roles and protect data at rest or in use.
  - Adopting the principle of least privilege for service accounts, administrators, or developers and using role-based access control (RBAC) or attribute-based access control (ABAC) to enforce granular permissions.
  - Leveraging the cloud-native features and services of Azure to achieve secure isolation and least privilege, such as Azure Active Directory, Azure Key Vault, Azure Security Center, or Azure Policy.