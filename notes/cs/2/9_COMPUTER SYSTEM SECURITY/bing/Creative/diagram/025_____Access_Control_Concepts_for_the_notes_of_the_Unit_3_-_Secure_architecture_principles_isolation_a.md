### Access Control Concepts

Access control is a security technique that regulates who or what can view or use resources in a computing environment. It is a fundamental concept in security that minimizes risk to the business or organization. Access control is a feature of modern Zero Trust security philosophy, which applies techniques like explicit verification and least-privileged access to help secure sensitive information and prevent it from falling into the wrong hands.

Access control relies heavily on two key principles—authentication and authorization:

- Authentication involves identifying a particular user based on their login credentials, such as usernames and passwords, biometric scans, PINs, or security tokens.
- Authorization refers to giving a user the appropriate level of access as determined by access control policies. These processes are typically automated.

Access control models have a subject and an object. The subject—the human user—is the one trying to gain access to the object—usually the software.

Some of the common access control models are:

- Discretionary Access Control (DAC): The owner of the object decides who can access it and with what permissions.
- Mandatory Access Control (MAC): The system assigns a security label to each object and user, and enforces access based on the comparison of these labels.
- Role-Based Access Control (RBAC): The system grants access based on the role of the user in the organization, rather than the individual identity.
- Attribute-Based Access Control (ABAC): The system grants access based on the attributes of the user, the object, and the environment, and evaluates them against a set of policies.

Key concepts that make up access control are permissions, ownership of objects, inheritance of permissions, user rights, and object auditing:

- Permissions are the actions that a user can perform on an object, such as read, write, execute, delete, etc.
- Ownership of objects is the relationship between a user and an object that gives the user full control over the object.
- Inheritance of permissions is the process of propagating the permissions of a parent object to its child objects.
- User rights are the abilities that a user has to perform certain system-level tasks, such as logging on, changing the system time, shutting down the system, etc.
- Object auditing is the process of recording the events that occur on an object, such as who accessed it, when, and what actions they performed.

Access control is an essential component of computer system security, as it helps to protect the confidentiality, integrity, and availability of the system and its resources. Access control also helps to comply with the legal and regulatory requirements, such as the General Data Protection Regulation (GDPR), the Health Insurance Portability and Accountability Act (HIPAA), the Payment Card Industry Data Security Standard (PCI DSS), etc.