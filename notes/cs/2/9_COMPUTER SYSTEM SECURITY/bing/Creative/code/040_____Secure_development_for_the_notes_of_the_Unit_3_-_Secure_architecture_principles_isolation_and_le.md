### Secure development for the notes of the Unit 3 - Secure architecture principles isolation and least privilege

- Secure development is the process of designing, building, testing, and maintaining software systems that are resilient to cyberattacks and comply with security standards and regulations.
- Secure architecture principles are the guidelines and best practices for creating secure software systems that follow the principles of secure design.
- Isolation and least privilege are two of the most important secure architecture principles that aim to reduce the attack surface and limit the impact of a breach.
- Isolation means separating different components or layers of a system into independent and isolated units that have minimal interaction and dependency. Isolation can be achieved by using different techniques such as:
  - Process isolation: running each application or service in a separate process with its own memory space and resources.
  - Network isolation: using firewalls, subnets, virtual networks, or VPNs to restrict network access and communication between different parts of a system.
  - Data isolation: encrypting, hashing, or masking sensitive data and storing them in separate locations or databases with different access controls.
  - User isolation: creating different user accounts or roles with different permissions and privileges for accessing the system or its components.
- Least privilege means granting the minimum amount of access or authority that is necessary for a user, process, or component to perform its function. Least privilege can be achieved by using different techniques such as:
  - Role-based access control (RBAC): assigning predefined roles to users or processes based on their responsibilities and tasks, and granting them only the permissions that are required for their roles.
  - Attribute-based access control (ABAC): granting access to users or processes based on their attributes or characteristics, such as identity, location, time, or context, and enforcing policies that define the conditions and rules for access.
  - Mandatory access control (MAC): labeling data and resources with security levels or classifications, and enforcing policies that define the access rules based on the security levels of the subjects and objects.
  - Discretionary access control (DAC): allowing the owners or creators of data and resources to decide who can access them and how, and enforcing policies that reflect their decisions.
- The benefits of applying isolation and least privilege in secure development are:
  - Reducing the attack surface: by isolating and restricting the access to different parts of a system, the potential entry points and targets for attackers are reduced, making it harder for them to compromise the system or exploit its vulnerabilities.
  - Limiting the impact of a breach: by granting the minimum amount of privileges to users or processes, the damage or harm that can be caused by a compromised or malicious user or process is limited, preventing them from accessing or affecting other parts of the system or data that are not related to their function.
  - Improving the security posture: by following the principles of isolation and least privilege, the system becomes more secure, compliant, and resilient to cyberattacks, enhancing its security posture and reputation.