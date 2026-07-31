# Access Control Concepts

Access control is a security technique that regulates who or what can view or use resources in a computing environment. It is a feature of modern Zero Trust security philosophy, which applies techniques like explicit verification and least-privileged access to help secure sensitive information and prevent it from falling into the wrong hands. Access control relies heavily on two key principles—authentication and authorization:

- Authentication involves identifying a particular user based on their login credentials, such as usernames and passwords, biometric scans, PINs, or security tokens.
- Authorization refers to giving a user the appropriate level of access as determined by access control policies. These policies can be based on factors such as the user's role, the resource's sensitivity, the time of day, or the location of access.

Access control models have a subject and an object. The subject—the human user—is the one trying to gain access to the object—usually the software. There are different types of access control models, such as:

- Discretionary Access Control (DAC): This model allows the owner of the object to decide who can access it and what level of access they have. For example, a file owner can grant read, write, or execute permissions to other users or groups.
- Mandatory Access Control (MAC): This model enforces a strict hierarchy of security levels, where each subject and object is assigned a security label, such as top secret, secret, or confidential. Access is granted only if the subject's security level is equal to or higher than the object's security level.
- Role-Based Access Control (RBAC): This model assigns permissions to roles rather than individual users, and users are assigned to roles based on their job functions. For example, a manager role can have access to financial reports, while an employee role can have access to customer data.
- Attribute-Based Access Control (ABAC): This model uses attributes of the subject, object, and environment to define access policies. For example, a policy can state that only users with a certain clearance, working on a certain project, and accessing from a certain device can view a certain document.

Key concepts that make up access control are permissions, ownership of objects, inheritance of permissions, user rights, and object auditing:

- Permissions are the actions that a subject can perform on an object, such as read, write, delete, or execute. Permissions can be granted or denied, and can be combined to form effective permissions.
- Ownership of objects refers to the ability of a subject to control the access to an object. The owner of an object can change its permissions, transfer its ownership, or delete it.
- Inheritance of permissions refers to the process of propagating permissions from a parent object to a child object. For example, a folder can inherit permissions from its parent folder, and a file can inherit permissions from its containing folder.
- User rights are the actions that a subject can perform on a system, such as logging on, changing the system time, or shutting down the system. User rights are controlled by security policies and can be assigned to users or groups.
- Object auditing refers to the process of recording and reviewing the events related to an object, such as who accessed it, when, and what actions they performed. Object auditing can help detect unauthorized access, track changes, or troubleshoot issues.

Access control is an essential component of computer system security, as it helps protect the confidentiality, integrity, and availability of resources from unauthorized or malicious access. Access control can also help enforce the principles of isolation and least privilege, which are key to secure architecture design:

- Isolation refers to the separation of different components or layers of a system, such as data, processes, or networks, to limit the impact of a potential compromise or failure. For example, a system can use firewalls, virtual machines, or encryption to isolate sensitive data or functions from other parts of the system.
- Least privilege refers to the principle of granting the minimum level of access necessary for a subject to perform its function, and revoking it when no longer needed. For example, a system can use role-based access control, temporary tokens, or multifactor authentication to ensure that users only have access to the resources they need for their tasks[^2^