Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 3 - Secure architecture principles isolation and least privilege.

## Unit 3 - Secure architecture principles isolation and least privilege

- Isolation and least privilege are two important principles for designing secure architectures.
- Isolation means separating different components or layers of a system from each other, so that a compromise or failure of one component does not affect the others.
- Least privilege means granting the minimum amount of access or permissions to each component or user of a system, so that they can only perform the tasks they need to and nothing more.
- These principles help to reduce the attack surface, limit the impact of incidents, and enforce the separation of duties and responsibilities.

### Isolation

- Isolation can be achieved at different levels of a system, such as network, host, application, and data.
- Network isolation involves creating boundaries or segments between different parts of a network, such as subnets, firewalls, routers, and gateways. This helps to prevent unauthorized access, contain network traffic, and isolate faults.
- Host isolation involves separating different processes or applications running on the same host, such as using containers, virtual machines, sandboxes, or chroot environments. This helps to prevent interference, resource contention, and privilege escalation.
- Application isolation involves separating different modules or components of an application, such as using microservices, APIs, or middleware. This helps to improve modularity, scalability, and maintainability.
- Data isolation involves separating different types of data or databases, such as using encryption, hashing, masking, or tokenization. This helps to protect the confidentiality, integrity, and availability of data.

### Least privilege

- Least privilege can be applied to different entities or actors of a system, such as users, processes, applications, and devices.
- User least privilege involves granting the minimum amount of access or permissions to each user of a system, such as using role-based access control (RBAC), attribute-based access control (ABAC), or mandatory access control (MAC). This helps to prevent unauthorized actions, data leakage, and identity theft.
- Process least privilege involves granting the minimum amount of privileges or capabilities to each process running on a system, such as using Linux capabilities, AppArmor, or SELinux. This helps to prevent malicious code execution, memory corruption, and system compromise.
- Application least privilege involves granting the minimum amount of resources or services to each application running on a system, such as using API keys, OAuth, or certificates. This helps to prevent unauthorized access, data manipulation, and service disruption.
- Device least privilege involves granting the minimum amount of functionality or connectivity to each device connected to a system, such as using device management, whitelisting, or blacklisting. This helps to prevent device tampering, malware infection, and network intrusion.